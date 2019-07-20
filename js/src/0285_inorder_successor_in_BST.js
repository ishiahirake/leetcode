/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @return {TreeNode}
 */
let inorderSuccessor = function(root, p) {
  return findInorderSuccessor(root, p, null)
};

function findInorderSuccessor(root, p, possible) {
  if (!root) {
    return null
  }

  if (p.val < root.val) {
    return findInorderSuccessor(root.left, p, root)
  }

  if (p.val > root.val) {
    return findInorderSuccessor(root.right, p, possible)
  }

  // When root.val equals to p.val, then find the inorder successor by following step:
  // 1. if the right node of the root is null, return possible
  // 2. if the right node of the root is none left,
  //    find the right node's left-most descendant node.
  let target = root.right
  if (target === null) {
    return possible
  }

  while (target.left !== null) {
    target = target.left
  }

  return target
}