<script lang="ts">
	import { page } from '$app/stores';
	import * as Tooltip from '$lib/components/ui/tooltip/index.js';
	import {
		LayoutDashboard,
		ClipboardList,
		ShoppingBag,
		Users,
		ChartNoAxesCombined,
		Settings
	} from 'lucide-svelte/icons';

	const navItems = [
		{ href: '/dashboard', icon: LayoutDashboard, label: 'Dashboard' },
		{ href: '/orders', icon: ClipboardList, label: 'Orders' },
		{ href: '/products', icon: ShoppingBag, label: 'Products' },
		{ href: '/customers', icon: Users, label: 'Customers' },
		{ href: '/analytics', icon: ChartNoAxesCombined, label: 'Analytics' },
		{ href: '/settings', icon: Settings, label: 'Settings' }
	];

	$: activeItem = $page.url.pathname.split('/')[1] || 'dashboard';
</script>

<aside
	class="fixed inset-y-0 left-0 z-10 hidden w-14 flex-col border-r bg-background pt-10 sm:flex"
>
	<nav class="flex flex-col items-center gap-4 px-2 py-4">
		{#each navItems as { href, icon: Icon, label }}
			<Tooltip.Root>
				<Tooltip.Trigger asChild let:builder>
					<a
						{href}
						class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
						href.slice(1)
							? 'bg-accent text-accent-foreground'
							: ''}"
						use:builder.action
						{...builder}
					>
						<Icon class="h-5 w-5" />
						<span class="sr-only">{label}</span>
					</a>
				</Tooltip.Trigger>
				<Tooltip.Content side="right">{label}</Tooltip.Content>
			</Tooltip.Root>
		{/each}
	</nav>
</aside>
