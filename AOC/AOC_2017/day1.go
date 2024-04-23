package main 

import (
  "fmt"
  "os"
)

func check(e error){
  if e != nil{
    panic(e)
  }

}


func main(){
  data, err := os.ReadFile("1.in")
  check(err)
  datastr := string(data)
  var digits []int

  for _, char := range(datastr){
    if char >= '0' && char <= '9' {
      d := int(char - '0')
      digits = append(digits, d)
    }
  }
  
  sum := 0
  for i := 1; i < len(digits); i++ {
    if digits[i] == digits[i -1] {
      sum += digits[i]
    }
  }
  first := digits[0]
  last := digits[len(digits) - 1]

  if first == last {
    sum += digits[0]
  }

  fmt.Println(sum)
}
