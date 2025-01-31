package main

import (
	"fmt"
)

const (
  SpanishLang = "Spanish"
  FrenchLang = "French"

  EnglishGreeting = "Hello, "
  SpanishGreeting = "Hola, "
  FrenchGreeting = "Bonjour, "
)

func Hello(name, language string) string {
  if name == "" {
    name = "World"
  }

  return greetingPrefix(language) + name + "!"
}

func greetingPrefix(language string) (greeting string) {
  switch language {
  case SpanishLang:
    greeting = SpanishGreeting
  case FrenchLang:
    greeting = FrenchGreeting
  default:
    greeting = EnglishGreeting
  }
  return
}

func main() {
	fmt.Println(Hello("Val",""))
}
