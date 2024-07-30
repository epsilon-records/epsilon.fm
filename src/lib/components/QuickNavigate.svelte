<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar/index.js';
	import { page } from '$app/stores';
</script>

<Menubar.RadioGroup value={$page.url.pathname.split('/')[1] || 'dashboard'}>
	{#each ['dashboard', 'music', 'orders', 'products', 'customers', 'analytics'] as item, index}
		<a href="/{item}">
			<Menubar.RadioItem disabled={$page.url.pathname.startsWith(`/${item}`)} value={item}>
				{item.charAt(0).toUpperCase() + item.slice(1)}
				<Menubar.Shortcut>⇧⌘{index + 1}</Menubar.Shortcut>
			</Menubar.RadioItem>
		</a>
	{/each}
</Menubar.RadioGroup>
