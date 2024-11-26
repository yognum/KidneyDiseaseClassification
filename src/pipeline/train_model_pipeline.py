import logging
import tensorflow as tf
import keras

from keras.api.applications.vgg16 import VGG16


class BaseModel:

    def get_vgg16_model(self):
        model = VGG16(weights='imagenet', include_top=False, input_shape=([224, 224, 3]))
        self.save_model(model, 'vgg16_model.h5')
        return model

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = keras.layers.Flatten()(model.output)
        prediction = keras.layers.Dense(classes, activation='softmax')(flatten_in)
        full_model = keras.Model(inputs=model.input, output=prediction)

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model

    def update_vgg16_model(self, model):
        model = self._prepare_full_model(
            model=model,
            classes=2,
            freeze_all=False,
            freeze_till=None,
            learning_rate=0.01
        )
        self.save_model(model, 'vgg16_model_updated.h5')

    @staticmethod
    def save_model(model, model_path):
        model.save(model_path)


try:
    base_model = BaseModel()
    base_model = base_model.get_vgg16_model()
    updated_base_model = base_model.update_vgg16_model()
    logging.info(f"Updated VGG16 model done")
except Exception as e:
    logging.error(f"getting error on base model: {e}")
    raise e
