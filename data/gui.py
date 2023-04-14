import random
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QGraphicsEllipseItem, QGraphicsScene, QGraphicsView, QLineEdit, QGraphicsLineItem, QGraphicsTextItem, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QPen, QBrush, QIntValidator
from PyQt6.QtCore import Qt

from centralizedGraph import CentralizedGraph
from decentralizedGraph import DecentralizedGraph


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 100, 1200, 800)
        self.setWindowTitle("Routing Algorithm Simulator")
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)

        self.UIComponents()

        self.show()

    def UIComponents(self):
        self.centralizedButton = QPushButton("Centralized Algorithm", self)
        self.centralizedButton.setGeometry(50, 50, 150, 40)
        self.centralizedButton.move(300, 250)
        self.centralizedButton.pressed.connect(
            lambda: self.algorithmWindow("centralized"))

        self.decentralizedButton = QPushButton("Decentralized Algorithm", self)
        self.decentralizedButton.setGeometry(50, 50, 150, 40)
        self.decentralizedButton.move(700, 250)
        self.decentralizedButton.pressed.connect(
            lambda: self.algorithmWindow("decentralized"))

    def algorithmWindow(self, type):
        self.w = algorithmWindow(type)
        self.w.show()
        self.hide()


class algorithmWindow(QWidget):
    def __init__(self, type):
        super().__init__()
        self.setGeometry(400, 100, 1200, 800)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(350, 0, 10, 10)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.algorithm = type
        self.graph = None
        self.nodes = []
        self.nodePos = []
        self.lines = [[None for _ in range(8)] for _ in range(8)]

        self.label = QLabel("", self)
        self.layout.addWidget(self.label)

        self.errorLabel = QLabel("Choose from 3 to 8 Nodes", self)
        self.errorLabel.setGeometry(0, 0, 200, 30)
        self.errorLabel.move(10, 70)

        self.weightTable = QTableWidget(self)
        self.weightTable.hide()

        if type == "centralized":
            self.setWindowTitle("Centralized Algorithm")
            self.label.setText("Dijikstra's Algorithm")
        else:
            self.setWindowTitle("Decentralized Algorithm")
            self.label.setText("Bellman-Ford Algorithm")

        self.UIComponents()

        self.show()

    def UIComponents(self):

        gv = QGraphicsView(self)
        gv.setFixedSize(650, 650)
        gv.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        gv.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.layout.addWidget(gv)
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 650, 600)
        gv.setScene(self.scene)

        homeButton = QPushButton("Home Page", self)
        homeButton.setGeometry(50, 50, 150, 40)
        homeButton.move(5, 5)
        homeButton.pressed.connect(self.homeWindow)

        inputBox = QLineEdit(self)
        inputBox.setPlaceholderText("# of Nodes")
        inputBox.setMaxLength(1)
        validator = QIntValidator(self)
        validator.setRange(3, 9)
        inputBox.setValidator(validator)
        inputBox.setGeometry(25, 25, 100, 30)
        inputBox.move(175, 107)

        generateGraphButton = QPushButton("Generate Graph", self)
        generateGraphButton.setGeometry(50, 50, 150, 40)
        generateGraphButton.move(5, 100)
        generateGraphButton.pressed.connect(
            lambda: self.generateGraph(inputBox.text()))

        self.nextIterationButton = QPushButton("Next Iteration", self)
        self.nextIterationButton.setEnabled(False)
        self.nextIterationButton.setGeometry(50, 50, 150, 40)
        self.nextIterationButton.move(5, 150)
        self.nextIterationButton.pressed.connect(self.nextIteration)

        self.setLayout(self.layout)

    def resetGraph(self):
        self.scene.clear()
        self.nodes = []
        self.nodePos = []
        self.currentNode = 0
        self.lines = [[None for _ in range(8)] for _ in range(8)]
        self.previousEdge = None
        self.nextIterationButton.setText("Next Iteration")
        self.nextIterationButton.setEnabled(True)
        self.nextIterationButton.setStyleSheet("color: black")

    def generateGraph(self, numNodes):
        if (numNodes != "" and int(numNodes) >= 3):
            self.resetGraph()
            if (self.algorithm == "centralized"):
                self.graph = CentralizedGraph(int(numNodes))
            else:
                self.graph = DecentralizedGraph(int(numNodes))
            self.drawNodes(int(numNodes))
            self.drawEdges()
            self.drawTable()
            self.errorLabel.setText("Choose from 3 to 8 Nodes")
            self.errorLabel.setStyleSheet("color: black")
        else:
            self.errorLabel.setText("Please enter a valid number of nodes")
            self.errorLabel.setStyleSheet("color: red")

    def drawNode(self, node, x, y):
        circle = QGraphicsEllipseItem(0, 0, 75, 75)
        circle.setPen(QPen(Qt.GlobalColor.black, 4, Qt.PenStyle.SolidLine))
        circle.setBrush(QBrush(Qt.GlobalColor.gray))
        circle.setPos(x, y)
        circle.text = QGraphicsTextItem(str(node), circle)
        circle.text.setPos(30, 27)
        self.nodePos.append({node: (x + 40, y + 40)})
        self.scene.addItem(circle)
        self.nodes.append(circle)

    def drawNodes(self, numNodes):
        self.resetGraph()

        self.drawNode(0, 200, 25)
        self.drawNode(1, 400, 25)
        self.drawNode(2, 25, 150)

        if (numNodes >= 4):
            self.drawNode(3, 25, 350)

        if (numNodes >= 5):
            self.drawNode(4, 550, 150)

        if (numNodes >= 6):
            self.drawNode(5, 550, 350)

        if (numNodes >= 7):
            self.drawNode(6, 200, 500)

        if (numNodes >= 8):
            self.drawNode(7, 400, 500)

        self.nodes[self.currentNode].setPen(
            QPen(Qt.GlobalColor.green, 4, Qt.PenStyle.SolidLine))

    def drawEdge(self, node1, node2, weight):
        node1Pos = self.nodePos[node1][node1]
        node2Pos = self.nodePos[node2][node2]

        if (self.lines[node1][node2] == None):
            drawLine = QGraphicsLineItem(
                node1Pos[0], node1Pos[1], node2Pos[0], node2Pos[1])
            drawLine.setPen(QPen(Qt.GlobalColor.black,
                            4, Qt.PenStyle.SolidLine))
            drawLine.text = QGraphicsTextItem(str(weight), drawLine)
            drawLine.text.setPos(node1Pos[0] + (node2Pos[0] - node1Pos[0]) / 2,
                                 node1Pos[1] + (node2Pos[1] - node1Pos[1]) / 2)

            drawLine.setZValue(-1)
            self.lines[node1][node2] = drawLine
            self.lines[node2][node1] = drawLine
            self.scene.addItem(drawLine)

    def drawEdges(self):
        maxEdges = self.graph.nodes * (self.graph.nodes - 1) / 3
        numEdges = 0

        for node in range(self.graph.nodes):
            randNode = random.randint(0, self.graph.nodes-1)
            while randNode == node:
                randNode = random.randint(0, self.graph.nodes-1)

            weight = random.randint(1, 10)
            self.graph.addEdge(node, randNode, weight)
            numEdges += 1

        while numEdges < maxEdges:
            node1 = random.randint(0, self.graph.nodes-1)
            node2 = random.randint(0, self.graph.nodes-1)

            if node1 != node2 and (self.graph.getEdge(node1, node2) == 0 or self.graph.getEdge(node1, node2) == None):
                weight = random.randint(1, 10)
                self.graph.addEdge(node1, node2, weight)
                numEdges += 1

        for i in range(self.graph.nodes):
            for j in range(self.graph.nodes):
                if self.graph.getEdge(i, j) != 0 and self.graph.getEdge(i, j) != None:
                    self.drawEdge(i, j, self.graph.getEdge(i, j))

    def drawTable(self):
        self.weightTable.setFixedSize(825, 55)
        self.weightTable.setRowCount(1)
        self.weightTable.setColumnCount(self.graph.nodes)
        self.weightTable.setHorizontalHeaderLabels(
            [str(i) for i in range(self.graph.nodes)])

        for i in range(self.graph.nodes):
            self.weightTable.setItem(0, i, QTableWidgetItem("inf"))

        self.weightTable.setItem(0, self.currentNode, QTableWidgetItem("0"))

        self.layout.addWidget(self.weightTable)
        self.weightTable.show()

    def nextIteration(self):
        self.nodes[self.graph.currentNode].setPen(
            QPen(Qt.GlobalColor.black, 4, Qt.PenStyle.SolidLine))
        if self.lines[self.graph.currentNode][self.graph.nextNode] != None:
            self.lines[self.graph.currentNode][self.graph.nextNode].setPen(
                QPen(Qt.GlobalColor.black, 4, Qt.PenStyle.SolidLine))

        if self.graph.finished:
            self.nextIterationButton.setEnabled(False)
            self.nextIterationButton.setText("Finished")
            self.nextIterationButton.setStyleSheet("color: green")

        self.graph.minPathFindIterative()
        self.weightTable.setItem(0, self.graph.nextNode, QTableWidgetItem(
            str(self.graph.getCost(self.graph.nextNode))))

        self.nodes[self.graph.currentNode].setPen(
            QPen(Qt.GlobalColor.green, 4, Qt.PenStyle.SolidLine))
        if self.lines[self.graph.currentNode][self.graph.nextNode] != None:
            self.lines[self.graph.currentNode][self.graph.nextNode].setPen(
                QPen(Qt.GlobalColor.red, 4, Qt.PenStyle.SolidLine))

    def homeWindow(self):
        w.show()
        self.close()


app = QApplication(sys.argv)
w = MainWindow()
app.exec()
