package main

import "testing"

func TestHello(t *testing.T) {
	t.Run("Saying hello to person", func(t *testing.T) {
		got := Hello("Val","")
		want := "Hello, Val!"
		assertCorrectMessage(t, got, want)
	})
	t.Run("Saying 'Hello World!' when no name is provided", func(t *testing.T) {
		got := Hello("","")
		want := "Hello, World!"
		assertCorrectMessage(t, got, want)
	})
  t.Run("..in Spanish", func(t *testing.T) {
    got := Hello("Val", "Spanish")
    want := "Hola, Val!"
    assertCorrectMessage(t, got, want)
  })
  t.Run("..in French", func(t *testing.T) {
    got := Hello("Val", "French")
    want := "Bonjour, Val!"
    assertCorrectMessage(t, got, want)
  })
}

func assertCorrectMessage(t testing.TB, got, want string) {
	t.Helper()
	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}
