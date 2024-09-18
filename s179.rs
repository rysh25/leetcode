pub struct Solution;

impl Solution {
    /// - Time complexity: O(n * k * log n)
    /// - Space complexity: O(1)
    ///
    /// #Greedy
    pub fn largest_number(nums: Vec<i32>) -> String {
        let mut str_vec: Vec<String> = nums.into_iter().map(|x| x.to_string()).collect();

        str_vec.sort_by(|a, b: &String| {
            let sa = format!("{}{}", a, b);
            let sb = format!("{}{}", b, a);
            sb.cmp(&sa)
        });

        if str_vec[0] == "0" {
            return "0".to_string();
        }

        str_vec.join("")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::largest_number(vec![10, 2]), "210");
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::largest_number(vec![3, 30, 34, 5, 9]), "9534330");
    }
}
