/**
 * 236. Lowest Common Ancestor of a Binary Tree.
 *
 * @see https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/
 */

// noinspection ES6ConvertVarToLetConst

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  return findLowestCommonAncestor(root, p, q, {})
};

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @param nodeTargetCountMap
 * @return {TreeNode}
 */
function findLowestCommonAncestor(root, p, q, nodeTargetCountMap) {
  if (!root) {
    return null;
  }

  let ancestor = findLowestCommonAncestor(root.left, p, q, nodeTargetCountMap)
  if (ancestor) {
    return ancestor
  }

  ancestor = findLowestCommonAncestor(root.right, p, q, nodeTargetCountMap)
  if (ancestor) {
    return ancestor
  }

  const leftTargetNodeCount = root.left ? nodeTargetCountMap[root.left.val] : 0
  const rightTargetNodeCount = root.right ? nodeTargetCountMap[root.right.val] : 0

  let nodeTargetNodeCount = 0
  if (root.val === p.val || root.val === q.val) {
    nodeTargetNodeCount = 1
  }

  nodeTargetNodeCount += (leftTargetNodeCount + rightTargetNodeCount)
  if (nodeTargetNodeCount === 2) {
    return root
  }

  nodeTargetCountMap[root.val] = nodeTargetNodeCount

  return null
}