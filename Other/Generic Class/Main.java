public class Main {
    
    public static void main(String[] args) {
        MyList<Car<?>> Cars = new MyList<>("Cars");
        Cars.Add(new Car<>("Volvo", "XC60", 2014, "D4", 2));
        Cars.Add(new Car<>("Audi", "R8", 2018, "T4S", 5.2f));

        for (int i = 0; i < Cars.getSize(); i++) {
            System.out.println(Cars.get(i).getMake());
            System.out.println(Cars.get(i).getModel());
            System.out.println(Cars.get(i).getYear());
            System.out.println(Cars.get(i).getEngine());
            System.out.println(Cars.get(i).getEngineVolume());
            System.out.println();
        }

        MyList<House<?>> Houses = new MyList<>("Houses");
        Houses.Add(new House<>(59222.99f, 7, 15));
        Houses.Add(new House<>(3000, 5, 2));

        for (int i = 0; i < Houses.getSize(); i++) {
            System.out.println(Houses.get(i).getPrice());
            System.out.println(Houses.get(i).getRooms());
            System.out.println(Houses.get(i).getAge());
            System.out.println();
        }
    }
   
}