import java.util.Arrays;

public class SumOfTwo {
	public static void main(String[] args){
		int[] numbers = Arrays.stream(args[0].split(", ")).mapToInt(Integer::parseInt).toArray();
		int value = Integer.parseInt(args[1]);
		System.out.println(hasSum(numbers, value));
	}

	public static boolean hasSum(int[] numbers, int value) {
		int arr_size = numbers.length;
		Arrays.sort(numbers);
		int left = 0, right = arr_size-1;
		while (left<right) {
			if (numbers[left]+numbers[right] == value)
				return true;
			else if (numbers[left]+numbers[right] < value)
				left++;
			else
				right--;
		}
		return false;
	}
}