pub struct Solution;

impl Solution {
    // - Time complexity: O(n)
    // - Space complexity: O(|s1|)
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let len1 = s1.len();
        let len2 = s2.len();
        if len1 > len2 {
            return false;
        }

        let mut count: [i32; 26] = [0; 26];
        let a_ascii = 'a' as usize;

        for i in 0..len1 {
            count[s1.chars().nth(i).unwrap() as usize - a_ascii] += 1;
            count[s2.chars().nth(i).unwrap() as usize - a_ascii] -= 1;
        }

        if count.iter().all(|&x| x == 0) {
            return true;
        }

        for i in len1..len2 {
            count[s2.chars().nth(i).unwrap() as usize - a_ascii] -= 1;
            count[s2.chars().nth(i - len1).unwrap() as usize - a_ascii] += 1;

            if count.iter().all(|&x| x == 0) {
                return true;
            }
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::check_inclusion("ab".to_string(), "eidbaooo".to_string()),
            true
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::check_inclusion("ab".to_string(), "eidboaoo".to_string()),
            false
        );
    }
}
