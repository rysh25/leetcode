pub struct Solution;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    /// - Time complexity: O(m * n)
    /// - Space compleixty: O(m * n)
    ///
    /// #LinkedList
    pub fn spiral_matrix(m: i32, n: i32, head: Option<Box<ListNode>>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = vec![vec![-1; n as usize]; m as usize];

        let (mut i, mut j) = (0, 0);

        let mut d = 0;
        let di: [i32; 4] = [0, 1, 0, -1];
        let dj: [i32; 4] = [1, 0, -1, 0];

        let mut curr = head.as_ref();

        while let Some(node) = curr {
            ans[i as usize][j as usize] = node.val;

            let (ni, nj) = (i + di[d], j + dj[d]);
            if ni < 0 || nj < 0 || m <= ni || n <= nj || ans[ni as usize][nj as usize] != -1 {
                d = (d + 1) % 4;
            }
            curr = node.next.as_ref();
            i += di[d];
            j += dj[d];
        }

        ans
    }
}
