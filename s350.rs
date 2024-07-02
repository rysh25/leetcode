pub struct Solution;

impl Solution {
    /// 2 つの整数配列 nums1 と nums2 を指定すると、それらの共通部分の配列を返します。
    /// 結果の各要素は、両方の配列に表示されている回数だけ出現する必要があり、結果は任意の順序で返すことができます。
    ///
    /// #TwoPointers
    ///
    /// - Time complexity: O(n)
    /// - Space complexity: O(1)
    pub fn intersect(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> Vec<i32> {
        let mut i1 = 0;
        let mut i2 = 0;
        let mut ans: Vec<i32> = vec![];

        nums1.sort();
        nums2.sort();
        // eprintln!("nums1={:?}, nums2={:?}", nums1, nums2);

        while i1 < nums1.len() || i2 < nums2.len() {
            // eprintln!("1 i1={:?}, i2={:?}", i1, i2);
            while i1 < nums1.len() && i2 < nums2.len() && nums1[i1] < nums2[i2] {
                i1 += 1;
            }

            while i1 < nums1.len() && i2 < nums2.len() && nums1[i1] > nums2[i2] {
                i2 += 1;
            }

            if i1 == nums1.len() || i2 == nums2.len() {
                break;
            }

            // eprintln!("2 i1={:?}, i2={:?}", i1, i2);

            if nums1[i1] == nums2[i2] {
                ans.push(nums1[i1]);
                i1 += 1;
                i2 += 1;
            }
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
            Solution::intersect(vec![1, 2, 2, 1], vec![2, 2]),
            vec![2, 2]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::intersect(vec![4, 9, 5], vec![9, 4, 9, 8, 4]),
            vec![4, 9]
        );
    }
}
