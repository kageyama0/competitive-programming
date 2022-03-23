use proconio::{input, marker::Chars};
use std::collections::HashMap;
use std::process;


fn main() {
    input! {
        n: usize, // u32にすると、for文でs[i]と指定すると、エラーになる
        xy: [(u32, u32); n],
        s: Chars,
    }

    let mut left_people = HashMap::new();
    let mut right_people = HashMap::new();

    for i in 0..n {
        let dir = s[i];
        let x_pos = xy[i].0;
        let y_pos = xy[i].1;

        if dir == 'R'{
            if left_people.contains_key(&y_pos) {
                if x_pos < left_people.get(&y_pos){
                    print("Yes")
                    process.exit(0);
                }
            }

            if right_people.contains_key(&y_pos){
                right_people.insert(y_pos, min(x_pos, right_people.get(&y_pos));
            }else{
                right_people.insert(y_pos, x_pos);
            }
        }


        if dir == 'L'{
            if right_people.contains_key(&y_pos){
                if x_pos > right_people.get(&y_pos){
                    print("Yes")
                    process::exit(0);
                }
            }

            if left_people.contains_key(&y_pos){
                left_people.insert(y_pos, max(x_pos, left_people.get(&y_pos));
            }else{
                left_people.insert(y_pos,x_pos);
            }
        }


    }


    println!("No");

}
