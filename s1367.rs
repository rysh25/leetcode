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
// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    /// - Time complexity: O(m * n)
    /// - Time complexity: O(h + n)
    ///
    /// - n: Length of the linked list
    /// - m: Number of nodes in the binary tree
    ///
    /// #LinkedList #BinaryTree
    pub fn is_sub_path(head: Option<Box<ListNode>>, root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::is_sub_path_core(&head, root, true)
    }

    fn is_sub_path_core(
        head: &Option<Box<ListNode>>,
        root: Option<Rc<RefCell<TreeNode>>>,
        is_head: bool,
    ) -> bool {
        if head.is_none() {
            return true;
        }

        if root.is_none() {
            return false;
        }

        let head = *head.clone().unwrap();

        let root = root.unwrap();
        let root = root.borrow();

        // println!(
        //     "head={:?}, root={:?}, is_head={:?}",
        //     head.val, root.val, is_head
        // );

        if head.val == root.val {
            if Self::is_sub_path_core(&head.next, root.left.clone(), false) {
                return true;
            }

            if Self::is_sub_path_core(&head.next, root.right.clone(), false) {
                return true;
            }

            if is_head
                && Self::is_sub_path_core(&Some(Box::new(head.clone())), root.left.clone(), true)
            {
                return true;
            }

            if is_head
                && Self::is_sub_path_core(&Some(Box::new(head.clone())), root.right.clone(), true)
            {
                return true;
            }
        } else {
            if is_head
                && Self::is_sub_path_core(&Some(Box::new(head.clone())), root.left.clone(), true)
            {
                return true;
            }

            if is_head
                && Self::is_sub_path_core(&Some(Box::new(head.clone())), root.right.clone(), true)
            {
                return true;
            }
        }

        false
    }
}
