use std::collections::HashSet;

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
    /// - Time complexity: O(n)
    /// - Space complexity: O(n)
    pub fn modified_list(nums: Vec<i32>, head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let s: HashSet<i32> = HashSet::from_iter(nums);

        let mut dummy = Box::new(ListNode::new(0));
        let mut prev = &mut dummy;
        let mut cur = head;

        while let Some(mut node) = cur {
            cur = node.next.take();
            if !s.contains(&node.val) {
                prev.next = Some(node);
                prev = prev.next.as_mut().unwrap();
            }
        }

        prev.next = None;

        dummy.next
    }
}
