import java.util.ArrayList;

public class MyList<T> {
    private String listID;
    private ArrayList<T> List = new ArrayList<T>();

    public MyList(String listID) {
        this.listID = listID;
    }

    public void Add(T obj) {
        List.add(obj);
    }

    public void Remove(int index) {
        List.remove(index);
    }

    public T get(int index) {
        return List.get(index);
    }

    public int getSize() {
        return List.size();
    }
}