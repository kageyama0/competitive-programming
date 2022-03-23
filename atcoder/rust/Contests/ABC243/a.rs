use proconio::input;

fn main() {
    input! {
        v: i32,
        a: i32,
        b: i32,
        c: i32,
    }

    let mut rest = v % (a+b+c);
    // println!("{}", rest);

    let family = ["F", "M", "T"];
    let amount = [a, b, c];
    for i in 0..3 {
        // println!("{}", rest);
        rest -= amount[i];
        if rest < 0{
            println!("{}", family[i]);
            break
        }
    }
}
