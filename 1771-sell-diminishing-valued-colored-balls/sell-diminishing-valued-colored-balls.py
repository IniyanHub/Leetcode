class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        inventory.sort(reverse=True)
        inventory.append(0)

        def get_sum(high, low):
            # Sum from low to high (inclusive)
            return (high * (high + 1) // 2) - ((low - 1) * low // 2)

        ans = 0
        count = 1

        for i in range(len(inventory) - 1):
            if orders == 0:
                break

            curr = inventory[i]
            nxt = inventory[i + 1]

            diff = curr - nxt
            need = diff * count

            if orders >= need:
                # Sell all values from curr down to nxt + 1
                ans += count * get_sum(curr, nxt + 1)
                ans %= MOD
                orders -= need
            else:
                # Only partially reduce the current highest stacks
                full = orders // count
                extra = orders % count

                # Sell 'full' complete levels
                ans += count * get_sum(curr, curr - full + 1)

                # Sell remaining 'extra' balls
                ans += extra * (curr - full)

                return ans % MOD

            count += 1

        return ans % MOD
        