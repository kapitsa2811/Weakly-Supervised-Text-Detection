#-*- coding: utf-8 -*-
from src.model_builder import CamModelBuilder

from keras.optimizers import Adam
from keras.applications.resnet50 import preprocess_input
from src.keras_utils import build_generator, create_callbacks

if __name__ == "__main__":
    
    model_builder = CamModelBuilder()
    model = model_builder.get_cls_model()
    model.summary()

#     fixed_layers = []
#     for layer in model.layers[:-6]:
#         layer.trainable = False
#         fixed_layers.append(layer.name)
#     print(fixed_layers)
 
    optimizer = Adam(lr=1e-3, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.005)
    model.compile(loss = 'categorical_crossentropy',
                  optimizer = optimizer,
                  metrics = ['accuracy'])
       
    train_generator = build_generator("dataset//train", preprocess_input, augment=True)
    model.fit_generator(train_generator,
                        steps_per_epoch = len(train_generator),
                        callbacks = create_callbacks(),
                        epochs=20)

