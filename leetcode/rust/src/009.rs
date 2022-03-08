// -2^31 <= x <= 2^31 - 1
// 4294967296 <= x <= 4294967295

impl Solution {
    pub fn is_palindrome(mut x: i32) -> bool {
        if x < 0 {
            return false;
        }

        let mut nums = Vec::with_capacity(10);
        // 各位の数字をnumsに収納する。
        while x != 0{
            nums.push(x % 10);
            x /= 10;
        }

        let len = nums.len();
        for i in 0..(len / 2){
            if nums[i] != nums[len-i-1]{
                return false;
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_009() {
        assert_eq!(true, Solution::is_palindrome(121);
        assert_eq!(false, Solution::is_palindrome(-120));
        assert_eq!(false, Solution::is_palindrome(10));
    }
}
