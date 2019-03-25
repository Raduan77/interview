import UIKit
// simple solution with use of hashtable
func sumOfTwo(array: [Int], result: Int) -> Bool {
    var storage: [Int: Any] = Dictionary()
    for index in 0..<array.count {
        if storage[result - array[index]] != nil {
            return true
        }
        storage[array[index]] = true
    }
    return false
}
assert(sumOfTwo(array: [10, 5, 17, 2, 15], result: 15) == true, "Test 1 failed")
assert(sumOfTwo(array: [5], result: 10) == false, "Test 2 failed")
assert(sumOfTwo(array: [5, 9, 3, 3, 4, 8, 15, 32, 10, 12], result: 10) == false, "Test 3 failed")
assert(sumOfTwo(array: [], result: 4) == false, "Test 4 failed")
print("All tests passed!")
