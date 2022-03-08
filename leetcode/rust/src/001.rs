pub struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let len = nums.len();
        for i in 0..(len-1){
            for j in i+1..len{
                if nums[j] == target - nums[i]{
                    return vec![i as i32, j as i32]
                }
            }
        }
        vec![]
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_001() {
        assert_eq!(vec![0, 1], Solution::two_sum(vec![2, 7, 11, 15], 9));
        assert_eq!(vec![1, 2], Solution::two_sum(vec![3, 2, 4], 6));
    }
}
