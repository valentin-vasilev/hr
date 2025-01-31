package main

import "fmt"

const Greeting = "Hello, "
func Hello(name string) string {
  if name == "" {
    name = "World"
  }
	return Greeting + name + "!"
}

func main() {
	fmt.Println(Hello("Val"))
}
