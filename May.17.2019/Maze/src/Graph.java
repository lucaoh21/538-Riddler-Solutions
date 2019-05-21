import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Graph {
	
//	private Map<Integer, ArrayList<Vertex>> neighbors;
	private Map<Integer, String> edgeColors;
	private Vertex[][] graph;
	private int xLength, yLength;
	
	public Graph(int xLength, int yLength) {
//		neighbors = new HashMap<Integer, ArrayList<Vertex>>();
		edgeColors = new HashMap<Integer, String>();
		graph = new Vertex[xLength][yLength];
		this.xLength = xLength;
		this.yLength = yLength;
	}
	
	public void addVertex(int xCoor, int yCoor) {
		Vertex vert = new Vertex(xCoor, yCoor);
		graph[yCoor][xCoor] = vert;
//		neighbors.put(vert.getCode(), new ArrayList<Vertex>());
	}
		
	public void addEdge(int x1, int y1, int x2, int y2, String color) {
		Integer code1 = graph[y1][x1].getCode();
		Integer code2 = graph[y2][x2].getCode();
		edgeColors.put((((code1 + code2) * (code1 + code2 + 1)) / 2 + code2), color);
		edgeColors.put((((code2 + code1) * (code2 + code1 + 1)) / 2 + code1), color);
	}
	
	public String printGraph() {
		StringBuilder string = new StringBuilder();
		for (int i = 0; i < yLength; i++) {
			for (int j = 0; j < xLength; j++) {
				string.append("[" + graph[i][j].getxCoor() + "," + graph[i][j].getyCoor() +"]");
			}
			string.append("\n");
		}
		return string.toString();
	}

//	public Map<Integer, ArrayList<Vertex>> getNeighbors() {
//		return neighbors;
//	}
//
//	public void setNeighbors(Map<Integer, ArrayList<Vertex>> neighbors) {
//		this.neighbors = neighbors;
//	}

	public Map<Integer, String> getEdgeColors() {
		return edgeColors;
	}

	public void setEdgeColors(Map<Integer, String> edgeColors) {
		this.edgeColors = edgeColors;
	}

	public Vertex[][] getGraph() {
		return graph;
	}

	public void setGraph(Vertex[][] graph) {
		this.graph = graph;
	}

	public int getxLength() {
		return xLength;
	}

	public void setxLength(int xLength) {
		this.xLength = xLength;
	}

	public int getyLength() {
		return yLength;
	}

	public void setyLength(int yLength) {
		this.yLength = yLength;
	}

}
