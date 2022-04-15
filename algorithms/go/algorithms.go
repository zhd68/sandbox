package main

import (
	"fmt"
	"math/rand"
)

func main() {
	myArrayInt := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 101, 102}
	myEmptyArrayInt := []int{}
	myDescArrayInt := []int{102, 101, 91, 72, 56, 38, 23, 16, 12, 8, 5, 2}
	itemInt := 2

	fmt.Println("Binary search iteration/бинарный поиск итерациями:")
	fmt.Println(binarySearchIteration(myArrayInt, itemInt))
	fmt.Println(binarySearchIteration(myEmptyArrayInt, itemInt))
	fmt.Println(binarySearchIteration(myDescArrayInt, itemInt))

	fmt.Println("Binary search recursion/бинарный поиск рекурсией:")
	fmt.Println(binarySearchRecursion(myArrayInt, itemInt))
	fmt.Println(binarySearchRecursion(myEmptyArrayInt, itemInt))
	fmt.Println(binarySearchRecursion(myDescArrayInt, itemInt))

	myUnsortedArrayInt := []int{1, 5, 7, 2, 2, 5, 90, 10}

	fmt.Println("Search smallest/поиск наименьшего")
	fmt.Println(searchSmallest(myUnsortedArrayInt))

	fmt.Println("Selection sort/сортировка выбором:")
	fmt.Println(selectionSort(myUnsortedArrayInt))

	fmt.Println("Quick sort/быстрая сортировка:")
	fmt.Println(quickSort(myUnsortedArrayInt))

}

func binarySearchIteration(dataArray []int, item int) (result bool, step int) {
	if len(dataArray) == 0 {
		return false, 0
	}

	low := 0
	high := len(dataArray) - 1
	reverse := false
	step = 0

	if dataArray[0] > dataArray[len(dataArray)-1] {
		reverse = true
	}

	for low <= high {

		mid := (low + high) / 2
		guess := dataArray[mid]
		step += 1

		switch {
		case guess == item:
			return true, step
		case guess > item && !reverse:
			high = mid - 1
		case guess < item && !reverse:
			low = mid + 1
		case guess > item && reverse:
			low = mid + 1
		case guess < item && reverse:
			high = mid - 1
		}
	}

	return false, step
}

func binarySearchRecursion(dataArray []int, item int) bool {
	if len(dataArray) == 0 {
		return false
	}

	if len(dataArray) == 1 {
		if dataArray[0] == item {
			return true
		} else {
			return false
		}
	}

	low := 0
	high := len(dataArray) - 1
	reverse := false
	mid := (low + high) / 2
	guess := dataArray[mid]

	if dataArray[0] > dataArray[len(dataArray)-1] {
		reverse = true
	}

	switch {
	case guess == item:
		return true
	case guess > item && !reverse:
		return binarySearchRecursion(dataArray[:mid], item)
	case guess < item && !reverse:
		return binarySearchRecursion(dataArray[mid+1:], item)
	case guess > item && reverse:
		return binarySearchRecursion(dataArray[mid+1:], item)
	case guess < item && reverse:
		return binarySearchRecursion(dataArray[:mid], item)
	}
	return false
}

func searchSmallest(dataArray []int) (smallestIdx int) {
	smallestIdx = 0

	for i := 1; i < len(dataArray); i++ {
		if dataArray[i] < dataArray[smallestIdx] {
			smallestIdx = i
		}
	}

	return smallestIdx
}

func selectionSort(dataArray []int) (sortedArray []int) {
	oldDataArray := make([]int, len(dataArray))
	copy(oldDataArray, dataArray)
	smallestIdx := 0
	lenDataArray := len(oldDataArray)

	for i := 0; i < lenDataArray; i++ {
		smallestIdx = searchSmallest(oldDataArray)
		sortedArray = append(sortedArray, oldDataArray[smallestIdx])
		oldDataArray[smallestIdx] = oldDataArray[len(oldDataArray)-1]
		oldDataArray = oldDataArray[:len(oldDataArray)-1]
	}

	return sortedArray
}

func quickSort(dataArray []int) []int {
	if len(dataArray) < 2 {
		return dataArray
	}

	pivotIdx := rand.Intn(len(dataArray))
	left, right := 0, len(dataArray)-1

	dataArray[pivotIdx], dataArray[right] = dataArray[right], dataArray[pivotIdx]

	for i := range dataArray {
		if dataArray[i] < dataArray[right] {
			dataArray[i], dataArray[left] = dataArray[left], dataArray[i]
			left++
		}
	}

	dataArray[left], dataArray[right] = dataArray[right], dataArray[left]

	quickSort(dataArray[:left])
	quickSort(dataArray[left+1:])

	return dataArray
}
