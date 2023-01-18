from datetime import datetime
import re
import math


roomAndTimeSpring = {'Mo': {'NAC 0/201': [570, 645, 660, 735, 780, 830, 850, 900, 930, 1005, 1110, 1160],
                            'NAC 5/123': [480, 564, 570, 654, 660, 744, 840, 960, 1110, 1194, 1200, 1275],
                            'NAC 4/121B': [480, 564, 570, 654, 660, 744, 750, 834, 840, 924, 930, 1014, 1020, 1104,
                                           1110, 1194], 'NAC 1/201': [720, 825, 1020, 1130],
                            'NAC 5/101': [750, 825, 840, 915], 'NAC 7/107': [840, 940],
                            'NAC 7/118': [840, 940, 960, 1060], 'NAC 1/203': [600, 750, 800, 825, 1050, 1170],
                            'NAC 1/202': [720, 830], 'NAC 3/225': [840, 970, 1010, 1160], 'NAC 3/224': [840, 915],
                            'NAC 5/213': [1170, 1320], 'NAC 7/313A': [570, 654, 660, 744, 840, 924, 1010, 1160],
                            'NAC 3/217': [1010, 1160], 'NAC 5/206': [1170, 1320],
                            'NAC 4/113': [600, 700, 750, 825, 840, 915, 960, 1070, 1110, 1185],
                            'NAC 4/115': [600, 660, 735, 750, 800, 825, 1080, 1180],
                            'NAC 6/122': [570, 654, 660, 744, 840, 940, 1110, 1185],
                            'NAC 6/112': [600, 660, 735, 800, 1110, 1185], 'NAC 6/311': [1020, 1104, 1110, 1185],
                            'NAC 5/111': [600, 750, 800, 825, 1080, 1180], 'NAC 1/301Z': [480, 555, 570, 645],
                            'NAC 6/308': [1005, 1115], 'NAC 6/304': [1005, 1115, 1125, 1235],
                            'NAC 4/108': [1020, 1095, 1110, 1194], 'NAC 5/150': [570, 654, 660, 744, 840, 924],
                            'NAC 7/227': [840, 924, 1110, 1194], 'NAC 5/142': [930, 1005], 'NAC 5/124': [840, 915],
                            'NAC 5/126': [570, 645, 1080, 1180], 'NAC 4/156': [570, 645], 'NAC 6/313': [660, 735],
                            'NAC 7/306': [840, 915], 'NAC 6/106': [840, 915], 'NAC 6/328': [750, 825],
                            'NAC 6/314': [660, 735, 750, 825, 1110, 1194],
                            'NAC 6/115': [570, 645, 720, 820, 840, 915, 1080, 1180],
                            'NAC 4/209': [720, 820, 960, 1060],
                            'NAC 6/114': [480, 580, 720, 820, 840, 940, 960, 1060, 1080, 1180],
                            'NAC 6/113': [480, 580, 600, 700, 720, 820, 840, 940, 960, 1060],
                            'NAC 6/111': [480, 580, 600, 720, 800, 820, 840, 940],
                            'NAC 5/102': [750, 825, 840, 915, 960, 1060, 1080, 1180],
                            'NAC 4/130': [720, 820, 960, 1060], 'NAC 5/108': [840, 940],
                            'NAC 5/109': [840, 940, 960, 1060], 'NAC 1/511E': [600, 700, 750, 825],
                            'NAC 6/121': [720, 820, 1110, 1185], 'NAC 1/302': [660, 735, 930, 1080],
                            'NAC 6/150': [480, 605, 630, 755, 840, 965],
                            'NAC 6/325': [570, 645, 660, 735, 750, 825, 840, 915, 930, 1005],
                            'NAC 7/218': [570, 620, 705, 755, 810, 860, 870, 920],
                            'NAC 7/320': [570, 645, 645, 695, 705, 755],
                            'NAC 5/110': [660, 735, 750, 825, 930, 1005, 1110, 1185],
                            'NAC 7/220': [750, 825, 930, 980, 990, 1040, 1110, 1160],
                            'NAC 7/236': [480, 555, 570, 645, 660, 735, 750, 825, 930, 1005, 1020, 1095],
                            'NAC 7/231': [570, 720], 'NAC 7/225': [1110, 1185], 'NAC 8/132C': [960, 1140],
                            'NAC 7/119': [930, 1080], 'NAC 4/222': [570, 654, 660, 735, 930, 1014],
                            'NAC 6/310': [660, 744], 'NAC 7/305': [660, 735, 1020, 1104, 1110, 1194],
                            'NAC 6/327': [660, 735]}, 'Tu': {'NAC 5/101': [660, 735, 840, 915],
                                                             'NAC 1/203': [570, 600, 645, 660, 735, 800, 840, 945,
                                                                           1050,
                                                                           1200],
                                                             'NAC 1/201': [720, 770, 930, 1005, 1020, 1095],
                                                             'NAC 6/313': [570, 654, 660, 744],
                                                             'NAC 7/118': [720, 820, 840, 940],
                                                             'NAC 7/107': [840, 940],
                                                             'NAC 6/113': [480, 555, 570, 645, 660, 735, 960, 1060,
                                                                           1080, 1180],
                                                             'NAC 5/111': [600, 660, 735, 800, 840, 940],
                                                             'NAC 6/112': [600, 660, 744, 800, 930, 1005],
                                                             'NAC 6/106': [660, 735, 840, 924, 930, 1005, 1020,
                                                                           1095,
                                                                           1110, 1185],
                                                             'NAC 6/121': [720, 840, 915, 930, 1080, 1180],
                                                             'NAC 0/201': [570, 620, 660, 735, 840, 915, 930, 1005],
                                                             'NAC 7/306': [840, 924, 930, 1005, 1020, 1095, 1155,
                                                                           1275],
                                                             'NAC 4/210': [660, 735, 840, 990],
                                                             'NAC 3/225': [840, 970, 1010, 1160],
                                                             'NAC 6/329': [750, 900], 'NAC 5/206': [1010, 1160],
                                                             'NAC 4/220': [1010, 1160], 'NAC 6/136': [1010, 1160],
                                                             'NAC 4/220C': [1010, 1160],
                                                             'NAC 4/130': [660, 735, 1080, 1180],
                                                             'NAC 6/310': [570, 654, 840, 924, 1110, 1185],
                                                             'NAC 6/122': [660, 744, 840, 915],
                                                             'NAC 4/222': [480, 564, 660, 735, 840, 924],
                                                             'NAC 5/124': [570, 654, 840, 915, 930, 1014, 1020,
                                                                           1095],
                                                             'NAC 4/113': [600, 700, 930, 1005, 1010, 1160],
                                                             'NAC 6/303': [1005, 1115],
                                                             'NAC 6/304': [1005, 1115, 1125, 1235],
                                                             'NAC 7/225': [840, 924],
                                                             'NAC 7/218': [480, 530, 540, 570, 590, 600, 650, 660,
                                                                           720,
                                                                           735, 840, 915, 930, 1005, 1020, 1095,
                                                                           1110,
                                                                           1260],
                                                             'NAC 6/327': [570, 645, 660, 735, 840, 924],
                                                             'NAC 6/328': [660, 735], 'NAC 7/227': [840, 924],
                                                             'NAC 4/121B': [480, 564, 660, 744],
                                                             'NAC 4/156': [660, 735, 840, 940, 960, 1060],
                                                             'NAC 5/110': [600, 700, 840, 915, 960, 1060, 1080,
                                                                           1180],
                                                             'NAC 6/115': [600, 700, 840, 940, 1020, 1095],
                                                             'NAC 5/102': [840, 940],
                                                             'NAC 4/115': [600, 700, 840, 940, 960, 1060, 1080,
                                                                           1180],
                                                             'NAC 6/111': [480, 580, 600, 800, 840, 915, 1110,
                                                                           1185],
                                                             'NAC 5/108': [600, 700],
                                                             'NAC 6/114': [480, 580, 600, 700, 840, 940, 960, 1060,
                                                                           1080, 1180],
                                                             'NAC 4/209': [660, 735, 840, 940, 960, 1060],
                                                             'NAC 5/109': [840, 940],
                                                             'NAC 5/126': [570, 645, 840, 915],
                                                             'NAC 1/302': [570, 695, 840, 915],
                                                             'NAC 1/511E': [1080, 1180], 'NAC 7/231': [840, 915],
                                                             'NAC 4/108': [570, 654],
                                                             'NAC 6/325': [570, 645, 660, 735, 840, 915, 1020,
                                                                           1095],
                                                             'NAC 7/220': [600, 750, 840, 990, 1020, 1095, 1110,
                                                                           1185],
                                                             'NAC 6/214': [840, 915],
                                                             'NAC 7/236': [480, 555, 570, 645, 660, 735, 1020,
                                                                           1170],
                                                             'NAC 8/130': [585, 705],
                                                             'NAC 8/110': [585, 705, 840, 950],
                                                             'NAC 8/103': [585, 705, 840, 950],
                                                             'NAC 8/132C': [840, 950],
                                                             'NAC 7/320': [570, 720, 840, 990, 1080, 1230],
                                                             'NAC 6/150': [880, 1080], 'NAC 7/312': [840, 924],
                                                             'NAC 1/301Y': [930, 1005], 'NAC 7/305': [660, 735]},
                     'We': {'NAC 0/201': [570, 645, 660, 735, 780, 830, 850, 900, 930, 1005, 1110, 1160],
                            'NAC 5/123': [480, 564, 570, 654, 660, 744, 840, 960, 1110, 1194, 1200, 1275],
                            'NAC 4/121B': [480, 564, 570, 654, 660, 744, 750, 834, 840, 924, 930, 1014, 1020, 1104,
                                           1110, 1194], 'NAC 1/201': [720, 825, 1020, 1130],
                            'NAC 5/101': [750, 825, 840, 915], 'NAC 7/107': [840, 940],
                            'NAC 7/118': [840, 940, 960, 1060], 'NAC 1/202': [720, 830],
                            'NAC 3/225': [840, 970, 1010, 1160], 'NAC 3/224': [840, 915], 'NAC 4/161': [1010, 1110],
                            'NAC 5/213': [1010, 1160], 'NAC 4/210': [840, 1005, 1010, 1160],
                            'NAC 3/218': [1010, 1160],
                            'NAC 7/313A': [570, 654, 660, 744, 840, 924, 1010, 1160], 'NAC 3/221': [1010, 1160],
                            'NAC 6/214': [1170, 1320], 'NAC 3/217': [1010, 1160],
                            'NAC 4/113': [600, 700, 750, 825, 840, 915, 960, 1070, 1110, 1185],
                            'NAC 4/115': [600, 660, 735, 750, 800, 825, 960, 1070, 1080, 1180],
                            'NAC 6/122': [570, 654, 660, 744, 840, 940, 1110, 1185],
                            'NAC 6/112': [600, 660, 735, 800, 1110, 1185], 'NAC 6/311': [1020, 1104, 1110, 1185],
                            'NAC 5/111': [600, 750, 800, 825, 1080, 1180], 'NAC 6/121': [720, 930, 1110, 1185],
                            'NAC 1/301Z': [480, 555, 570, 645], 'NAC 6/303': [1005, 1115, 1125, 1235],
                            'NAC 6/304': [1125, 1235], 'NAC 4/108': [1020, 1095, 1110, 1194],
                            'NAC 5/150': [570, 654, 660, 744, 840, 924], 'NAC 7/227': [840, 924, 1110, 1194],
                            'NAC 5/142': [930, 1005], 'NAC 5/124': [840, 915, 1010, 1130],
                            'NAC 5/126': [570, 645, 1080, 1180], 'NAC 4/156': [570, 645], 'NAC 6/313': [660, 735],
                            'NAC 7/306': [840, 915], 'NAC 6/106': [840, 915], 'NAC 6/328': [750, 825],
                            'NAC 6/314': [660, 735, 750, 825, 1110, 1194],
                            'NAC 6/115': [570, 645, 720, 820, 840, 915, 1080, 1180],
                            'NAC 4/209': [720, 820, 960, 1060],
                            'NAC 6/114': [480, 580, 720, 820, 840, 940, 960, 1060, 1080, 1180],
                            'NAC 6/113': [480, 580, 600, 700, 720, 820, 840, 940, 960, 1060],
                            'NAC 6/111': [480, 580, 600, 720, 800, 820, 840, 940],
                            'NAC 1/203': [600, 720, 750, 800, 825, 870],
                            'NAC 5/102': [750, 825, 840, 915, 960, 1060, 1080, 1180],
                            'NAC 4/130': [720, 820, 960, 1060], 'NAC 5/108': [840, 940],
                            'NAC 5/109': [840, 940, 960, 1060], 'NAC 1/511E': [600, 700, 750, 825],
                            'NAC 1/302': [660, 735, 930, 1080], 'NAC 6/295': [840, 1005], 'NAC 4/133': [840, 990],
                            'NAC 6/150': [480, 605, 630, 755, 840, 965],
                            'NAC 6/325': [570, 645, 660, 735, 750, 825, 840, 915, 930, 1005],
                            'NAC 7/218': [570, 620, 705, 755, 810, 860, 870, 920],
                            'NAC 7/320': [495, 545, 570, 645, 645, 695, 705, 755],
                            'NAC 5/110': [660, 735, 750, 825, 930, 1005, 1110, 1185],
                            'NAC 7/220': [750, 825, 930, 980, 990, 1040], 'NAC 7/119': [570, 720],
                            'NAC 7/236': [480, 555, 570, 645, 660, 735, 750, 825, 930, 1005, 1020, 1095],
                            'NAC 7/231': [570, 720], 'NAC 7/225': [1110, 1185],
                            'NAC 8/132C': [705, 825, 1020, 1140],
                            'NAC 8/131': [585, 705], 'NAC 4/222': [570, 654, 660, 735, 930, 1014],
                            'NAC 6/310': [660, 744], 'NAC 7/305': [660, 735, 1020, 1104, 1110, 1194],
                            'NAC 6/327': [660, 735]}, 'Th': {'NAC 5/101': [660, 735, 840, 915],
                                                             'NAC 1/203': [570, 600, 645, 660, 735, 800, 840, 945,
                                                                           1050,
                                                                           1200],
                                                             'NAC 5/123': [480, 564, 570, 654, 660, 744, 840, 960,
                                                                           1110,
                                                                           1194, 1200, 1275],
                                                             'NAC 4/121B': [480, 564, 570, 654, 660, 744, 750, 834,
                                                                            840,
                                                                            924, 930, 1014, 1020, 1104, 1110, 1194],
                                                             'NAC 1/201': [720, 770, 930, 1005, 1020, 1095],
                                                             'NAC 6/313': [570, 654, 660, 744],
                                                             'NAC 7/107': [840, 940],
                                                             'NAC 6/113': [480, 555, 570, 645, 660, 735, 960, 1060,
                                                                           1080, 1180],
                                                             'NAC 5/111': [600, 660, 735, 800, 840, 940],
                                                             'NAC 6/112': [600, 660, 744, 800, 930, 1005],
                                                             'NAC 6/106': [660, 735, 840, 924, 930, 1005, 1020,
                                                                           1095,
                                                                           1110, 1185],
                                                             'NAC 6/121': [720, 840, 915, 930, 1080, 1180],
                                                             'NAC 4/108': [570, 654, 960, 1010, 1110, 1194],
                                                             'NAC 0/201': [570, 620, 660, 735, 840, 915, 930, 1005],
                                                             'NAC 7/306': [840, 924, 930, 1005, 1020, 1095, 1155,
                                                                           1275],
                                                             'NAC 4/210': [660, 735, 840, 990],
                                                             'NAC 6/306': [570, 690],
                                                             'NAC 7/219': [930, 1080], 'NAC 6/307': [1010, 1110],
                                                             'NAC 5/126': [570, 645, 840, 915, 1010, 1130],
                                                             'NAC 4/222': [480, 564, 660, 735, 840, 924, 930, 1014,
                                                                           1140, 1260],
                                                             'NAC 3/225': [840, 970, 1010, 1160],
                                                             'NAC 3/217': [1010, 1160], 'NAC 5/215': [1010, 1210],
                                                             'NAC 5/213': [1010, 1160],
                                                             'NAC 4/130': [660, 735, 1080, 1180],
                                                             'NAC 6/310': [570, 654, 840, 924, 1110, 1185],
                                                             'NAC 6/122': [660, 744, 840, 915],
                                                             'NAC 5/124': [570, 654, 840, 915, 930, 1014, 1020,
                                                                           1095],
                                                             'NAC 6/303': [1005, 1115, 1125, 1235],
                                                             'NAC 6/308': [1005, 1115], 'NAC 7/225': [840, 924],
                                                             'NAC 6/311': [1020, 1104],
                                                             'NAC 7/227': [840, 924, 1110, 1194],
                                                             'NAC 7/218': [480, 530, 540, 570, 590, 600, 650, 660,
                                                                           720,
                                                                           735, 840, 915, 930, 1005, 1020, 1095,
                                                                           1110,
                                                                           1260],
                                                             'NAC 6/327': [570, 645, 660, 735, 840, 924],
                                                             'NAC 6/328': [660, 735],
                                                             'NAC 6/314': [660, 735, 750, 825, 1110, 1194],
                                                             'NAC 4/156': [660, 735, 840, 940, 960, 1060],
                                                             'NAC 5/110': [600, 700, 840, 915, 960, 1060, 1080,
                                                                           1180],
                                                             'NAC 6/115': [600, 700, 840, 940, 1020, 1095],
                                                             'NAC 5/102': [840, 940],
                                                             'NAC 4/115': [600, 700, 840, 940, 960, 1060, 1080,
                                                                           1180],
                                                             'NAC 6/111': [480, 580, 600, 800, 840, 915, 1110,
                                                                           1185],
                                                             'NAC 5/108': [600, 700],
                                                             'NAC 4/113': [600, 700, 930, 1005],
                                                             'NAC 6/114': [480, 580, 600, 700, 840, 940, 960, 1060,
                                                                           1080, 1180],
                                                             'NAC 4/209': [660, 735, 840, 940, 960, 1060],
                                                             'NAC 5/109': [840, 940],
                                                             'NAC 1/302': [570, 695, 840, 915],
                                                             'NAC 1/511E': [1080, 1180], 'NAC 6/295': [840, 1005],
                                                             'NAC 7/231': [840, 915],
                                                             'NAC 6/325': [570, 645, 660, 735, 840, 915, 1020,
                                                                           1095],
                                                             'NAC 7/220': [600, 750, 840, 990, 1020, 1095, 1110,
                                                                           1185],
                                                             'NAC 6/214': [840, 915],
                                                             'NAC 7/236': [480, 555, 570, 645, 660, 735, 1020,
                                                                           1170],
                                                             'NAC 8/132C': [585, 705], 'NAC 8/110': [840, 950],
                                                             'NAC 7/119': [570, 720, 840, 990],
                                                             'NAC 7/320': [600, 750, 840, 990],
                                                             'NAC 7/305': [660, 735, 1020, 1104, 1110, 1194],
                                                             'NAC 7/312': [840, 924], 'NAC 1/301Y': [930, 1005]},
                     'Fr': {'NAC 5/101': [570, 720], 'NAC 0/201': [615, 765], 'NAC 6/313': [570, 654, 660, 744],
                            'NAC 7/107': [540, 640, 660, 760], 'NAC 7/118': [540, 640, 660, 760],
                            'NAC 6/121': [720, 930, 960, 1010], 'NAC 5/102': [900, 950],
                            'NAC 4/156': [780, 830, 900, 950], 'NAC 5/109': [780, 830], 'NAC 5/110': [720, 770],
                            'NAC 5/111': [600, 750, 800, 800], 'NAC 7/225': [840, 924], 'NAC 6/122': [570, 654],
                            'NAC 5/150': [570, 654, 660, 744, 840, 924],
                            'NAC 7/313A': [570, 654, 660, 744, 840, 924],
                            'NAC 4/121B': [480, 564, 660, 744, 750, 834],
                            'NAC 6/310': [570, 654, 660, 744, 840, 924, 1080, 1230],
                            'NAC 6/112': [600, 660, 744, 800],
                            'NAC 7/227': [840, 924], 'NAC 4/222': [480, 564, 570, 654, 840, 924],
                            'NAC 1/203': [600, 720, 750, 800, 825, 870], 'NAC 4/115': [600, 800],
                            'NAC 6/111': [600, 800], 'NAC 4/108': [570, 654], 'NAC 7/218': [480, 530, 600, 650],
                            'NAC 7/220': [540, 590, 660, 710], 'NAC 7/236': [540, 690], 'NAC 6/106': [840, 924],
                            'NAC 5/124': [570, 654, 930, 1014], 'NAC 7/306': [840, 924], 'NAC 5/123': [480, 564],
                            'NAC 6/327': [840, 924], 'NAC 7/312': [840, 924]},
                     'Sa': {'NAC 5/111': [570, 820], 'NAC 6/150': [570, 870]}, 'Su': {}}


def timenow():
    currentTime = datetime.today().strftime("%I:%M%p")
    currentDay = 1  # int(datetime.today().strftime("%w"))
    week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    return week[currentDay], currentTime


def to_min(currentTime):
    time_min = 0

    timee = currentTime[:-2].split(":")  # gets one of the time and splits it to get hour and min
    # checks to see if the time contains "PM" and does not start with 12
    if currentTime.__contains__("PM") and timee[0] != "12":
        time_min = 60 * (int(timee[0])) + int(timee[1]) + 720
    else:
        time_min = 60 * (int(timee[0])) + int(timee[1])
    return time_min


def to_reg_time(min_time, change_time):
    time = ""

    if change_time:
        return min_time

    elif min_time >= 780:
        min_time = min_time - 720
        hour = math.floor(min_time / 60)
        minutes = '%02d' % math.ceil(((min_time / 60) - hour) * 60)
        time = str(hour) + ":" + str(minutes) + "PM"

    elif min_time < 780:
        hour = math.floor(min_time / 60)
        minutes = '%02d' % math.ceil(((min_time / 60) - hour) * 60)
        if min_time in range(720, 780):
            time = str(hour) + ":" + str(minutes) + "PM"
        else:
            time = str(hour) + ":" + str(minutes) + "AM"

    return time


def classRoom():
    currentTime = datetime.today().strftime("%I:%M%p")
    military = datetime.today().strftime("%H%M")
    currentDay = int(datetime.today().strftime("%w"))
    week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    product = {}
    if int(military) in range(0000, 630):
        product["Go HOME"] = ""
        return product

    min_cur_time = to_min(currentTime)
    for room in roomAndTimeSpring[week[currentDay]]:
        times = roomAndTimeSpring[week[currentDay]][room]  # room

        for i in range(1, len(times), 2):

            if i == len(times) - 1:
                if times[i] < min_cur_time:
                    product[room] = " IS FREE REST OF THE DAY!"
                break
            elif min_cur_time in range(times[i], times[i + 1]):
                minutes = to_reg_time((times[i + 1] - min_cur_time), True)
                product[room] = " IS FREE TILL " + to_reg_time(times[i + 1], False) + " YOU HAVE " + str(minutes) + " MINUTES LEFT TILL NEXT CLASS"

                break
    if product.__len__() == 0:
        product["NO EMPTY CLASS AVAILABLE RIGHT NOW COME BACK LATER"] = ""
    return product
