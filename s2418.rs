pub struct Solution;

impl Solution {
    /// - Time compleixty: O(n log n)
    /// - Space complexity: O(n)
    ///
    /// #Sort
    pub fn sort_people(names: Vec<String>, heights: Vec<i32>) -> Vec<String> {
        let mut indices: Vec<usize> = (0..names.len()).collect();
        indices.sort_by(|&a, &b| heights[b].cmp(&heights[a]));

        indices.iter().map(|&i| names[i].clone()).collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::sort_people(
                vec!["Mary".to_string(), "John".to_string(), "Emma".to_string()],
                vec![180, 165, 170],
            ),
            ["Mary", "Emma", "John"]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::sort_people(
                vec!["Alice".to_string(), "Bob".to_string(), "Bob".to_string()],
                vec![155, 185, 150]
            ),
            ["Bob", "Alice", "Bob"]
        );
    }
}
