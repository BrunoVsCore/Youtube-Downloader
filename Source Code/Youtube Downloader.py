# -*- coding: utf-8 -*-
# Created by: Bruno Irvayni Software

from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMessageBox,QFileDialog
from PySide2.QtGui import QImage, QPixmap,QIcon
from layout7 import Ui_MainWindow
from PySide2 import QtWidgets
from pytube import YouTube
import requests
import os


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #Codigo--------------------------------------------------------->>>

        def Baixar_Musica():

            conteudo = self.lineEdit_Inserir_url.text()
            yt = YouTube(conteudo)
            result = yt.streams.filter(only_audio=True).first()

            self.download.setText('Download: Baixando Música Aguarde... ')
            self.download.repaint()

            # Salvamento Música
            self.selected_directory = QtWidgets.QFileDialog.getExistingDirectory()
            if not self.selected_directory:
                self.download.setText('Download:')
                self.download.repaint()
                return
            output_file = result.download(self.selected_directory)
            path, _ = os.path.splitext(output_file)
            os.rename(output_file, path + '.mp3')


            #Local salvamento Música info
            self.download.setText('Download: Concluído MP3')
            msg = QMessageBox()
            msg.setText(f'Salvo em: {self.selected_directory}')
            msg.setWindowTitle('Download Concluído')
            icon = QIcon()
            icon.addFile(u":/newPrefix/download.ico", QSize(), QIcon.Normal, QIcon.Off)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon(icon))
            msg.exec()



        def Baixar_Video():
            conteudo = self.lineEdit_Inserir_url.text()
            yt = YouTube(conteudo)
            result = yt.streams.get_highest_resolution()

            #Label Baixando video
            self.download.setText('Download: Baixando Vídeo Aguarde...')
            self.download.repaint()

            #Salvamento
            self.selected_directory = QtWidgets.QFileDialog.getExistingDirectory()
            if not self.selected_directory:
                self.download.setText('Download:')
                self.download.repaint()

                return

            output_file = result.download(self.selected_directory)
            path, _ = os.path.splitext(output_file)
            os.rename(output_file, path + '.mp4')

            #Local salvamento Vídeo
            self.download.setText('Download: Concluído MP4')
            self.download.repaint()
            msg = QMessageBox()
            msg.setText(f'Salvo em: {self.selected_directory}')
            msg.setWindowTitle('Download Concluído')
            icon = QIcon()
            icon.addFile(u":/newPrefix/download.ico", QSize(), QIcon.Normal, QIcon.Off)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon(icon))
            msg.exec()



        #Botões Interações-------------------------------------------->>>


        def pesquisar():
            conteudo = self.lineEdit_Inserir_url.text()
            try:
                self.yt = YouTube(conteudo)
            except:
                self.nome.setText(f'Nome: {"Não foi possível encontrar a URL"}')
                self.nome.repaint()
                return


            self.nome.setText(f'Nome: {self.yt.title}')
            imagem = self.yt.thumbnail_url
            image = QImage()
            image.loadFromData(requests.get(imagem).content)

            self.foto_imagem.setScaledContents(True)
            self.foto_imagem.setMaximumSize(332,131)
            self.foto_imagem.setPixmap(QPixmap(image))







        self.botao_colarurl.clicked.connect(pesquisar)
        self.botao_baixar_musica.clicked.connect(Baixar_Musica)
        self.botao_baixar_video.clicked.connect(Baixar_Video)









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())






