from keras.models import Model, Sequential
from keras.layers import Dense
from PIL import Image
import numpy as np

def conimg(y):
    x = []
    for i in range(len(y)):
        img = Image.fromarray(y[i])
        imgs = img.resize(size=(32, 32))
        imgs = np.array(imgs)
        x.append(np.repeat(imgs[:, :, np.newaxis], 3, axis=2))
    x = np.array(x,dtype='float32')
    return x

def main(train_x,train_y,test_x):
    dim = train_x.shape[1]
    x = int(dim**(1/2)) +1
    y_train = np.argmax(train_y,axis=-1)
    classes = len(np.unique(y_train))
    model = Sequential()
    model.add(Dense(((x*x)-dim),name='feature', activation='relu',input_shape=(dim,)))
    model.add(Dense(classes,activation='softmax'))

    model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])

    # here, inputs and labels are same
    model.fit(train_x,train_y,epochs=100,batch_size=512,verbose=0)
    extract = Model(model.inputs, model.get_layer('feature').output)

    # predict whole inputs through it
    x1 = extract.predict(train_x)
    x2 = extract.predict(test_x)

    # concatenate on horizontal axis
    train_x = np.concatenate((train_x, x1), axis=1) 
    test_x = np.concatenate((test_x, x2), axis=1) 

    train_x = train_x.reshape(train_x.shape[0],x,x)
    test_x = test_x.reshape(test_x.shape[0],x,x)
    
    return conimg(train_x),conimg(test_x)
    
if __name__ == '__main__':
    main()