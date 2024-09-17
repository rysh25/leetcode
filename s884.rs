use std::collections::HashMap;

pub struct Solution;

impl Solution {
    // - Time complexity: O(|s1| + |s2|)
    // - Space complexity: O(|s1| + |s2|)
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut m: HashMap<&str, i32> = HashMap::new();

        s1.split_whitespace().for_each(|word| {
            *m.entry(word).or_insert(0) += 1;
        });

        s2.split_whitespace().for_each(|word| {
            *m.entry(word).or_insert(0) += 1;
        });

        m.iter()
            .filter(|&(_, &count)| count == 1)
            .map(|(&word, _)| word.to_string()) // キー（単語）だけを抽出
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::uncommon_from_sentences(
                "this apple is sweet".to_string(),
                "this apple is sour".to_string()
            ),
            ["sweet", "sour"]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::uncommon_from_sentences("apple apple".to_string(), "banana".to_string()),
            ["banana"]
        );
    }
}
