
import numpy as np
if __name__ == '__main__':
	a = np.array([[0.53461923, 0.51567645, 0.63654055, 0.94668209, 0.65837958],
       [0.99999294, 0.99999212, 0.99999996, 1.00001129, 0.99999908],
       [1.000001  , 0.94666342, 0.91030862, 0.95304011, 0.95250329],
       [0.        , 0.05462217, 0.94538088, 0.55621271, 0.38905394],
       [0.64106991, 0.79738744, 0.70608289, 0.61332389, 0.68946604],
       [0.999971  , 0.99998521, 1.00000003, 0.99996545, 0.99998042],
       [0.24944354, 0.98323902, 0.00646908, 0.        , 0.30978791],
       [0.0091957 , 0.97459016, 0.15346543, 0.        , 0.28431282],
       [0.99995598, 0.99997919, 0.99994057, 0.99990293, 0.99994467],
       [0.59048137, 0.71148551, 0.99996461, 0.69296973, 0.74872531],
       [0.86073586, 0.89426124, 0.99999997, 0.9058898 , 0.91522172],
       [0.59962468, 0.82559689, 0.71512032, 0.58243806, 0.68069499],
       [0.99999929, 0.99989128, 0.99993865, 0.99990863, 0.99993446],
       [0.66154012, 0.87625737, 0.74651427, 0.62049936, 0.72620278],
       [0.        , 0.16035011, 0.99982646, 0.33994652, 0.37503077],
       [0.99588046, 0.99563972, 0.99955044, 0.99845863, 0.99738231],
       [0.99892442, 0.9998991 , 0.99994975, 0.99898792, 0.9994403 ],
       [0.65062659, 0.52006237, 0.69399943, 0.91815403, 0.69571061],
       [0.99998684, 0.99947495, 0.99990578, 0.99942776, 0.99969883],
       [0.99770113, 0.9995588 , 0.99906608, 0.99571916, 0.99801129],
       [0.30253975, 0.23040293, 0.31486726, 0.99766137, 0.46136783],
       [0.29000198, 0.27296272, 0.5865083 , 0.91413968, 0.51590317],
       [0.99999999, 0.99999999, 0.99999999, 0.99999999, 0.99999999],
       [0.1123401 , 0.        , 0.09462466, 1.00078355, 0.30193708],
       [1.00000995, 0.74770484, 0.52567659, 0.73781274, 0.75280103],
       [0.99999999, 1.0000035 , 0.99999782, 0.99999597, 0.99999932],
       [0.73210701, 0.97633078, 0.86501032, 0.73210649, 0.82638865],
       [0.99702953, 0.99859964, 0.99161748, 0.98911284, 0.99408987],
       [0.99999999, 0.30094345, 0.        , 0.16123792, 0.36554534],
       [0.98135821, 0.97963506, 0.99566487, 0.99710895, 0.98844177],
       [0.73360023, 0.65430835, 0.7946549 , 0.95051594, 0.78326985],
       [0.99999933, 0.99999948, 0.99999989, 0.99999974, 0.99999961],
       [0.99985534, 0.99911502, 0.99965878, 0.99823798, 0.99921678],
       [0.77037928, 0.87484209, 0.79547341, 0.64726814, 0.77199073],
       [0.86106531, 0.89443092, 0.90584729, 0.78328788, 0.86115785],
       [0.79172685, 0.69791583, 0.81444886, 0.92361909, 0.80692766],
       [0.99999378, 0.99999381, 1.00000075, 1.00000103, 0.99999734],
       [0.93084566, 0.86655458, 0.96973445, 0.95101117, 0.92953646],
       [0.        , 0.        , 0.99942051, 0.2561918 , 0.31390308],
       [0.99999999, 0.99684661, 0.99810931, 0.99679043, 0.99793658],
       [0.76737422, 0.8860541 , 0.80583645, 0.6741914 , 0.78336404],
       [0.        , 0.72414543, 0.81363402, 0.        , 0.38444486],
       [0.60131244, 0.77543044, 0.7163495 , 0.67794502, 0.69275935],
       [0.        , 0.23941839, 0.99999998, 0.11157776, 0.33774903],
       [0.8466159 , 0.85612826, 0.84095134, 0.74814301, 0.82295963],
       [0.18478223, 0.99951433, 0.06992971, 0.        , 0.31355657],
       [0.76409738, 0.85946955, 0.79086224, 0.69090206, 0.77633281],
       [0.81921298, 0.71233381, 0.80074933, 1.00655903, 0.83471379],
       [0.99976317, 0.95288685, 0.94042384, 0.94032541, 0.95834982],
       [0.50834414, 0.94415135, 0.00272595, 0.        , 0.36380536],
       [0.99999339, 0.99997673, 0.99996782, 0.99999912, 0.99998427],
       [0.99002445, 0.31257413, 0.31257413, 0.60845528, 0.555907  ],
       [0.69086858, 0.93971778, 0.17246001, 0.11243672, 0.47887077],
       [0.2860096 , 0.26154879, 0.28764624, 1.0014933 , 0.45917448],
       [0.03838901, 0.99793648, 0.1873101 , 0.        , 0.3059089 ],
       [0.95504438, 0.56154786, 0.51435783, 0.85530367, 0.72156344],
       [0.97328765, 0.52495201, 0.        , 0.00496662, 0.37580157],
       [0.99995258, 0.29224618, 0.        , 0.25018937, 0.38559703],
       [1.        , 0.93146326, 0.91024342, 0.93029845, 0.94300128],
       [0.99991313, 0.99989432, 0.99999705, 0.9999448 , 0.99993732],
       [0.78554568, 0.68641341, 0.80485428, 0.92008386, 0.79922431],
       [1.        , 1.        , 1.        , 1.        , 1.        ],
       [0.72788328, 0.88775918, 0.74679372, 0.68548266, 0.76197971],
       [0.96394769, 0.91085617, 0.92009421, 0.8583191 , 0.91330429]])
	print(str(a[np.argmax(a[:,4]),:])+" A")