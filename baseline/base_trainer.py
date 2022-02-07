"""
    File name: base_trainer.py
    Description: Base class for data loaders, you can create your own dataloader(class) based on this one.
                It could simplify your work.

    Author: Botian Lan
    Time: 2022/01/24
"""
from abc import abstractmethod, ABC
import logging
import torch
import pathlib


class BaseTrainer(ABC):
    def __init__(self, model, epoch, data_loader):
        self.model = model
        self.epoch = epoch
        self.data_loader = data_loader
        self.console_logger = logging.getLogger('console_loggers')
        self.train_logger = logging.getLogger('train_file_loggers')

    @abstractmethod
    def _epoch_train(self, epoch):
        """
         Train process for every epoch.
         Should be overridden by all subclasses.
        :param epoch: Specific epoch for one iteration.
        """
        raise NotImplementedError

    @abstractmethod
    def _epoch_val(self):
        """
         Train process for every epoch.
         Should be overridden by all subclasses.
        """
        raise NotImplementedError

    def _train(self):
        """
         Epoch-wise train logic.
        :return:
        """
        for epoch in range(self.epoch):
            self.console_logger.info(' Epoch {} begin'.format(epoch))
            self.train_logger.info(' Epoch {} begin'.format(epoch))
            self._epoch_train(epoch)
            self.model.train()

            # save model for every epoch
            self.save_model(self.model, epoch)

    # TODO: Untested
    def save_model(self, model, epoch):
        """
         Save model's parameters of every epoch into pkl file.
        :param model: train model
        :param epoch: current epoch number
        :return:
        """
        path = 'model/saved_model/'
        model_path = 'model/saved_model/model_state_dict_{}.pkl'.format(epoch)
        model_saved_path = pathlib.Path(path)
        if model_saved_path.is_dir():
            torch.save(model.state_dict(), 'model/saved_model/model_state_dict_{}.pkl'.format(epoch))
            self.console_logger.info('---------------- Model has been saved to "{}",epoch {} ----------------'
                                     .format(model_path, epoch))
            self.train_logger.info('---------------- Model has been saved to "{}",epoch {} ----------------'
                                     .format(model_path, epoch))

        else:
            raise FileNotFoundError("Model saved directory: '{}' not found!".format(path))

    # TODO: Untested
    def load_model(self, epoch):
        """
         Load saved model dict to
        :param epoch: choose a specific epoch number to load
        :return:
        """
        path = 'model/saved_model/model_state_dict_{}.pkl'.format(epoch)
        model_load_path = pathlib.Path(path)
        if model_load_path.is_file():
            model_params = torch.load(model_load_path)
            self.model.load_state_dict(model_params)

            self.console_logger.info('---------------- Model parameters of epoch {} has been loaded ----------------'
                                     .format(path, epoch))
        else:
            raise FileNotFoundError("Model state dict: '{}' not found!".format(path))


if __name__ == '__main__':
    """
        Abstractmethod test code.
    """
    class Train(BaseTrainer):
        def __init__(self, model, epoch, data_loader):
            super(Train, self).__init__(model, epoch, data_loader)

    train = BaseTrainer(1, 2, 3)

