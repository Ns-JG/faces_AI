from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.applications import vgg16
from keras.optimizers import RMSprop

class AI_transfer:
    
    conv_base=vgg16.VGG16(weights='imagenet', include_top=False, pooling='max', input_shape=(35,35,3))
    model = Sequential()
    model.add(conv_base)
    # TOP
    model.add(Dropout(.2))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=RMSprop(learning_rate=5e-5, momentum=.3), metrics=['acc'])