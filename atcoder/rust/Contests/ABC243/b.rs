use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
        b: [usize; n],
    }

    let mut cnt_x = 0;
    let mut cnt_y = 0;

    for i in 0..n {

        for j in 0..n{
            if a[i] == b[j]{
                if i == j{
                    cnt_x += 1
                }else{
                    cnt_y += 1;
                }
            }
        }
    }


    println!("{}", cnt_x);
    println!("{}", cnt_y);

}
