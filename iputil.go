package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
)

func main() {

    if len(os.Args) == 1 { help()}

    if os.Args[1] == "-4" { ipv4() }
    if os.Args[1] == "-6" { ipv6() }

    if os.Args[1] == "-h" { help() }
    if os.Args[1] == "-H" { help() }
    if os.Args[1] == "--help" { help() } else { help() }
}

func ipv4() {
    resp, err := http.Get("https://ipv4.icanhazip.com")
    if err != nil {
        fmt.Println(err)}
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println(err)}
    fmt.Print(string(body))
    os.Exit(0)
}

func ipv6() {
        resp, err := http.Get("https://ipv6.icanhazip.com")
        if err != nil {
                fmt.Println(err)}
        body, err := ioutil.ReadAll(resp.Body)
        if err != nil {
                fmt.Println(err)}
        fmt.Print(string(body))
    os.Exit(0)
}

func help() {
    fmt.Print(`The available switches are:
    -h, -H or --help Shows this command

    -4 shows your ipv4 address
    -6 shows your ipv6 address
`)
os.Exit(0)
}
