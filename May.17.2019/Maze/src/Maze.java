import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Maze {
	
	private static final String[] BLUE_COLORS = new String[] {"blue", "green", "purple", "white"};
	private static final String[] RED_COLORS = new String[] {"red", "orange", "purple", "white"};
	private static final String[] YELLOW_COLORS = new String[] {"yellow", "green", "orange", "white"};

	
	private static Graph maze;
	private static Set<String> colors;
	private static ArrayList<Vertex> path;
	private static ArrayList<String> sequence;
	
	public Maze() {
		
	}
	
	public static Graph constructRiddlerGraph() {
		maze = new Graph(9, 9);
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				maze.addVertex(j, i);
			}
		}

		String[][] xColors = new String[][] {
			{"green","purple","purple","white","purple","white","white","green"},
			{"red","blue","yellow","black","red","black","orange","blue"},
			{"yellow","red","blue","red","orange","white","green","red"},
			{"white","orange","orange","green","green","purple","yellow","green"},
			{"black","orange","blue","purple","black","green","purple","black"},
			{"white","green","blue","green","orange","blue","orange","purple"},
			{"yellow","purple","green","black","orange","blue","blue","green"},
			{"purple","black","red","blue","green","white","yellow","purple"},
			{"orange","purple","white","white","white","red","orange","green"}
		};
		
		String[][] yColors = new String[][] {
			{"white","red","white","yellow","purple","green","red","blue","orange"},
			{"yellow","white","green","purple","white","yellow","green","black","white"},
			{"white","black","orange","white","black","purple","yellow","black","red"},
			{"yellow","green","purple","green","orange","blue","orange","purple","orange"},
			{"white","purple","black","orange","red","purple","orange","blue","purple"},
			{"green","red","purple","orange","yellow","blue","black","orange","yellow"},
			{"white","black","white","orange","purple","red","white","red","orange"},
			{"orange","green","orange","blue","orange","black","white","blue","orange"}
		};
		
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 8; j++) {
				maze.addEdge(j, i, j+1, i, xColors[i][j]);
			}
		}
		
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 9; j++) {
				maze.addEdge(j, i, j, i+1, yColors[i][j]);
			}
		}
		
		//System.out.println(maze.printGraph());
				
		return maze;
	}
	
	public static boolean findPossiblePath(Vertex node) {
		node.setVisited(true);
		if (node.isEndNode()) {
			path.add(node);
			sequence.add("end");
			return true;
		}
		
		//checks left neighbor
		if (node.getxCoor() - 1 >= 0) {
			Vertex next = maze.getGraph()[node.getyCoor()][node.getxCoor()-1];
			int code = cantorPairing(node.getCode(), next.getCode());
			if (!next.isVisited() && colors.contains(maze.getEdgeColors().get(code))) {
				if (findPossiblePath(next)) {
					path.add(node);
					sequence.add("left");
					return true;
				}	
			}
		}
		
		//checks right neighbor
		if (node.getxCoor() + 1 < maze.getxLength()) {
			Vertex next = maze.getGraph()[node.getyCoor()][node.getxCoor()+1];
			int code = cantorPairing(node.getCode(), next.getCode());
			if (!next.isVisited() && colors.contains(maze.getEdgeColors().get(code))) {
				if (findPossiblePath(next)) {
					path.add(node);
					sequence.add("right");
					return true;
				}	
			}
		}
		
		//checks top neighbor
		if (node.getyCoor() - 1 >= 0) {
			Vertex next = maze.getGraph()[node.getyCoor()-1][node.getxCoor()];
			int code = cantorPairing(node.getCode(), next.getCode());
			if (!next.isVisited() && colors.contains(maze.getEdgeColors().get(code))) {
				if (findPossiblePath(next)) {
					path.add(node);
					sequence.add("up");
					return true;
				}	
			}
		}
		
		//checks bottom neighbor
		if (node.getyCoor() + 1 < maze.getyLength()) {
			Vertex next = maze.getGraph()[node.getyCoor()+1][node.getxCoor()];
			int code = cantorPairing(node.getCode(), next.getCode());
			if (!next.isVisited() && colors.contains(maze.getEdgeColors().get(code))) {
				if (findPossiblePath(next)) {
					path.add(node);
					sequence.add("down");
					return true;
				}	
			}
		}
				
		return false;
		
	}
	
	public static int cantorPairing (int x, int y) {
		return ((x + y) * (x + y + 1)) / 2 + y;
	}
	
	public static void main(String[] args) {
		
		colors = new HashSet<String>(Arrays.asList(RED_COLORS));
		path = new ArrayList<Vertex>();
		sequence = new ArrayList<String>();
		
		Graph maze = constructRiddlerGraph();
		maze.getGraph()[1][8].setEndNode(true);
		
		boolean foundPath = findPossiblePath(maze.getGraph()[7][0]);
		if (foundPath) {
			for (int i = 0; i < path.size(); i++) {
				System.out.println("[" + path.get(i).getxCoor() + "," + path.get(i).getyCoor() +"] " + sequence.get(i));
			}
		}
	}

}
