import pickle
import time
import numpy as np

from keras.preprocessing.image import ImageDataGenerator

from layer_data import LayerData
from util.image import ImageDataset


class NetworkData(object):

    def __init__(self, model, layers=None, dataset_path=None, num_max_activations=100, save_path=None):
        self.model = model
        # self.center_shift = center_shift
        self.layers = []
        self.build_layers(layers)
        self.dataset_path = dataset_path
        self.save_path = save_path
        self.num_max_activations = num_max_activations
        self.input_image_size = None
        self.dataset = None

    def build_layers(self, layers):
        if layers is not None:
            for l in layers:
                self.layers.append(LayerData(l))

    def eval_network(self, size_dataset, target_size=None, batch_size=32, **kwargs):

        times_ex = []
        self.input_image_size = target_size

        prep_function = kwargs.get('preprocessing_function')
        self.dataset = ImageDataset(self.dataset_path, target_size, prep_function)

        for layer in self.layers:

            datagen = ImageDataGenerator(**kwargs)
            data_batch = datagen.flow_from_directory(
                self.dataset_path,
                target_size=self.input_image_size,
                batch_size=batch_size,
                shuffle=False
            )

            start = time.time()
            num_images = size_dataset
            n_batches = 0
            # filters = None

            for i in data_batch:
                images = i[0]
                idx = (data_batch.batch_index - 1) * data_batch.batch_size
                file_names = data_batch.filenames[idx: idx + data_batch.batch_size]

                layer.evaluate_activations(file_names, images, self.model, self.num_max_activations, batch_size)

                print 'On layer ', layer.get_layer_id(), ', Get and sort activations in batch num: ', n_batches,
                ' Images processed: ', idx + data_batch.batch_size

                n_batches += 1
                if n_batches >= num_images / data_batch.batch_size:
                    break

            layer.set_max_activations()

            end_act_time = time.time() - start

            # pickle.dump(filters, open(self.save_path + layer.get_layer_id() + '.obj', 'wb'))

            layer.build_neuron_feature(self.dataset, self.model)

            end_comp_nf_time = time.time() - end_act_time - start

            print 'Time (s) to get and sort activations from ', num_images, ' images: ', end_act_time
            print 'Time (s) to compute_nf and receptive fields from each neuron: ', end_comp_nf_time

            times_ex.append(time.time() - start)

            # pickle.dump(layer.get_filters(), open(self.save_path + layer.get_layer_id() + '.obj', 'wb'))

        for i in xrange(len(times_ex)):
            print 'total time execution for layer ', i, ' : ', times_ex[i]

    def get_layers(self):
        return self.layers

    def save(self, file_name=None):
        if file_name is None:
            file_name = self.model.name

        pickle.dump(self, open(self.save_path + file_name + '.obj', 'wb'))

    # def load(self, file_name=None):
    #     if file_name is None:
    #         file_name = self.model.name
    #
    #     return pickle.load(open(file_name + '.obj', 'rb'))

    def selectivity_idx_summary(self, sel_index, layers, bin=None, labels=None, **kwargs):
        sel_idx_dict = dict()
        for index_name in sel_index:
            sel_idx_dict[index_name] = []
            for l in self.layers:
                if l.get_layer_id() in layers:
                    sel_idx_dict[index_name].append(l.get_selectivity_idx(
                        self.model, index_name, self.dataset, labels, **kwargs))

        return sel_idx_dict

    def similarity_index(self, layers):
        sim_idx = []
        for l in self.layers:
            if l.get_layer_id() in layers:
                sim_idx.append(l.get_similarity_idx(self.model, self.dataset))
        return sim_idx

    def get_max_activations(self, layer_id, img_name, location, num_max):
        layer = None
        if type(layer_id) is int:
            layer = self.layers[layer_id]
        if type(layer_id) is str:
            for l in self.layers:
                if layer_id == l.get_layer_id():
                    layer = l

        img = self.dataset.load_images([img_name])
        hc_activations, hc_idx = layer.decomposition_image(self.model, img)
        loc = layer.get_location_from_rf(location)

        activations = hc_activations[loc[0], loc[1], :num_max]
        neuron_idx = hc_idx[loc[0], loc[1], :num_max]

        f = layer.get_filters()
        neurons = []
        for idx in neuron_idx:
            neurons.append(f[int(idx)])

        return list(activations), neurons

    def decomposition(self, src_layer, target_layer, neuron_idx, overlapping=0.0):

        for l in self.layers:
            if src_layer == l.get_layer_id():
                src_layer = l
            elif target_layer == l.get_layer_id():
                target_layer = l

        hc_activations, hc_idx = src_layer.decomposition_nf(
            neuron_idx, target_layer, self.model, self.dataset)

        hc_activations = hc_activations[:, :, 0]
        hc_idx = hc_idx[:, :, 0]

        c_overlapping = 0.0
        while c_overlapping <= overlapping: #TODO: implement overlapping
            max_act = np.amax(hc_activations)
            pos = np.unravel_index(hc_activations.argmax(), hc_activations.shape)
            print pos
            neuron_idx = hc_idx[pos]

            print target_layer.receptive_field_map[pos]


            c_overlapping = 1

        print hc_activations
        print hc_idx.shape

        return None





    '''
    keras models cant be pickled. This is a workaround for deleting 
    the model property within the NetworkData class.
    Also the dataset property (ImageDataset class is deleted)
    '''
    def __getstate__(self):
        odict = self.__dict__
        odict['model'] = None
        odict['dataset'] = None
        return odict

    # def __setstate__(self, state):
    #     state['model'] = self.model
    #     self.__dict__ = state
