package main

import (
	"fmt"
	"strings"
)

func main() {
	var query string
	var number float64

	fmt.Println("=================")
	fmt.Print("文字列を入力: ")
	fmt.Scan(&query)
	num := str2num(query, 0.5, 0.3, 0.15, 0.05)
	fmt.Println(num)
	fmt.Println("=================")

	fmt.Print("算術符号を入力: ")
	fmt.Scan(&number)
	str := num2str(number, 0.5, 0.3, 0.15, 0.05)
	fmt.Println(str)
	fmt.Println("=================")
}

func str2num(query string, a float64, b float64, c float64, d float64) (float64) {
	front := map[string]float64{
		"a": 0.,
		"b": a,
		"c": a+b,
		"d": a+b+c,
	}

	var back = map[string]float64{
		"a": a,
		"b": a+b,
		"c": a+b+c,
		"d": a+b+c+d,
	}

	var lineWidth = map[string]float64{
		"a": a,
		"b": b,
		"c": c,
		"d": d,
	}
	queryArray := strings.Split(query, "")
	var value float64 = front[queryArray[0]]
	var width float64 = back[queryArray[0]]

	for i:=1; i<len(queryArray); i++ {
		value = value + width * front[queryArray[i]]
		width = width * lineWidth[queryArray[i]]
	}

	return value
}

func num2str(number float64, a float64, b float64, c float64, d float64) (string) {
	var front = map[string]float64{
		"a": 0.,
		"b": a,
		"c": a+b,
		"d": a+b+c,
	}

	var back = map[string]float64{
		"a": a,
		"b": a+b,
		"c": a+b+c,
		"d": a+b+c+d,
	}

	var lineWidth = map[string]float64{
		"a": a,
		"b": b,
		"c": c,
		"d": d,
	}
	
	var ans string = ""
	var letters []string = []string{"a", "b", "c", "d"}

	for number>0. {
		for i:=0; i<len(letters); i++ {
			if front[letters[i]] <= number && number < back[letters[i]] {
				ans += letters[i]
				number = (number - front[letters[i]]) / lineWidth[letters[i]]
			}
		}
	}
	
	return ans
}