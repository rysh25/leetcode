#[derive(Default)]
struct Trie {
    count: usize,
    children: [Option<Box<Trie>>; 27],
}

pub struct Solution;

impl Solution {
    /// - Time complexity: O(n * m)
    /// - Space complexity: O(n * m)
    ///
    /// #Trie
    pub fn sum_prefix_scores(words: Vec<String>) -> Vec<i32> {
        let n = words.len();
        let mut root = Trie::default();

        for word in &words {
            let mut curr = &mut root;

            for c in word.chars().map(|x| x as usize - 'a' as usize) {
                curr = curr.children[c].get_or_insert_with(Default::default);
                curr.count += 1;
            }
        }

        let mut ans: Vec<i32> = vec![0; n];

        for (i, word) in words.into_iter().enumerate() {
            let mut count = 0;
            let mut curr = &root;

            for c in word.chars().map(|x| x as usize - 'a' as usize) {
                curr = curr.children[c].as_ref().unwrap();
                count += curr.count;
            }

            ans[i] = count as _;
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::sum_prefix_scores(vec![
                "abc".to_string(),
                "ab".to_string(),
                "bc".to_string(),
                "b".to_string(),
            ],),
            [5, 4, 3, 2]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::sum_prefix_scores(vec!["abcd".to_string()]), [4]);
    }
}
