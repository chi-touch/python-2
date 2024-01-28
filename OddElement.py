public class OddElement{

	public void(int [] element){
	for(int i = 0; i < element.length; i+=2){
		System.out.print(element[i]+" ");
	}


    }

	public static void main(String[] args){
	OddElement value = new OddElent();

	int [] number = {1,2,3,4,5,6};
	value.odd(number);

	
}

}