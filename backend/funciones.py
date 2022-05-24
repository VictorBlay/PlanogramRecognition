import cv2
from backend.prepare_data import prepare_data

orb = cv2.ORB_create()

def find_des(images):
    des_list = []
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        des_list.append(des)
    return des_list

def find_id(img, des_list, thres = 15):
    kp2, des2 = orb.detectAndCompute(img, None)
    #print(kp2[0].pt, kp2[1].pt)
    bf = cv2.BFMatcher()
    match_list = []
    final_val = -1
    try:
        for des in des_list:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])
            match_list.append(len(good))
    except:
        print("error")
    if len(match_list) != 0:
        if max(match_list) > thres:
            final_val = match_list.index(max(match_list))
    return final_val

def imagenes(path):
    ruta_img = [i[0] for i in prepare_data(path)]
    imagenes = []
    for i in ruta_img:
        cap = cv2.imread(i)
        imagenes.append(cap)
    return imagenes

def car_prod(path):
    carpetas = [i[1] for i in prepare_data(path)]
    return carpetas

def convert(*args):
    """
    Returns a list of tuples generated from multiple lists and tuples
    """
    for x in args:
        if not isinstance(x, list) and not isinstance(x, tuple):
            return []

    size = float("inf")
    
    for x in args:
        size = min(size, len(x))
        
    result = []
    
    for i in range(size):
        result.append(tuple([x[i] for x in args]))
        
    return result