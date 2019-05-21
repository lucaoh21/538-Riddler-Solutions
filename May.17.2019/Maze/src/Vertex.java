
public class Vertex {
	private int xCoor, yCoor;
	private Integer code;
	private boolean inPath, visited, endNode;
	
	public Vertex(int xCoor, int yCoor) {
		this.xCoor = xCoor;
		this.yCoor = yCoor;
		code = new Integer(((xCoor + yCoor) * (xCoor + yCoor + 1)) / 2 + yCoor);
		inPath = false;
		visited = false;
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

	public Integer getCode() {
		return code;
	}

	public void setCode(Integer code) {
		this.code = code;
	}

	public boolean isInPath() {
		return inPath;
	}

	public void setInPath(boolean inPath) {
		this.inPath = inPath;
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

}
