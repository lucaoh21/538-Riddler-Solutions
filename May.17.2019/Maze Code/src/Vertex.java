import java.util.LinkedList;

public class Vertex {
	private int xCoor, yCoor, distance;
	private Integer code;
	private boolean visited, endNode;
	private LinkedList<Vertex> shortestPath;
	
	public Vertex(int xCoor, int yCoor) {
		this.xCoor = xCoor;
		this.yCoor = yCoor;
		code = new Integer(((xCoor + yCoor) * (xCoor + yCoor + 1)) / 2 + yCoor);
		distance = Integer.MAX_VALUE;
		visited = false;
		shortestPath = new LinkedList<Vertex>();
	}

	public int getxCoor() {
		return xCoor;
	}

	public void setxCoor(int xCoor) {
		this.xCoor = xCoor;
	}

	public int getyCoor() {
		return yCoor;
	}

	public void setyCoor(int yCoor) {
		this.yCoor = yCoor;
	}

	public int getDistance() {
		return distance;
	}

	public void setDistance(int distance) {
		this.distance = distance;
	}

	public Integer getCode() {
		return code;
	}

	public void setCode(Integer code) {
		this.code = code;
	}

	public boolean isVisited() {
		return visited;
	}

	public void setVisited(boolean visited) {
		this.visited = visited;
	}

	public boolean isEndNode() {
		return endNode;
	}

	public void setEndNode(boolean endNode) {
		this.endNode = endNode;
	}

	public LinkedList<Vertex> getShortestPath() {
		return shortestPath;
	}

	public void setShortestPath(LinkedList<Vertex> shortestPath) {
		this.shortestPath = shortestPath;
	}

}
