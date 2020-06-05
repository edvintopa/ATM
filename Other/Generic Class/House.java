public class House<T> {
    private T Price;
    private int Rooms;
    private int Age;
    

    public House(T Price, int Rooms, int Age) {
        this.Price = Price;
        this.Rooms = Rooms;
        this.Age = Age;
    }

    public T getPrice() { return this.Price; }
    public int getRooms() { return this.Rooms; }
    public int getAge() { return this.Age; }

    public void setMake(String Make) { this.Make = Make;}
    public void setRooms(int Rooms) { this.Rooms = Rooms;}
    public void setAge(int Age) { this.Age = Age;}
    
}