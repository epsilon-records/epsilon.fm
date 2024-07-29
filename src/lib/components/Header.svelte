<script lang="ts">
	import Breadcrumbs from './Breadcrumbs.svelte';
	import House from 'lucide-svelte/icons/house';
	import FileChartLine from 'lucide-svelte/icons/file-chart-line';
	import Package from 'lucide-svelte/icons/package';
	import Package2 from 'lucide-svelte/icons/package-2';
	import PanelLeft from 'lucide-svelte/icons/panel-left';
	import Search from 'lucide-svelte/icons/search';
	import ShoppingCart from 'lucide-svelte/icons/shopping-cart';
	import UsersRound from 'lucide-svelte/icons/users-round';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu/index.js';
	import OrganizationSwitcher from 'clerk-sveltekit/client/OrganizationSwitcher.svelte';
	import { Input } from '$lib/components/ui/input/index.js';
	import * as Sheet from '$lib/components/ui/sheet/index.js';
	import UserButton from 'clerk-sveltekit/client/UserButton.svelte';
	import Sun from 'lucide-svelte/icons/sun';
	import Moon from 'lucide-svelte/icons/moon';
	import { resetMode, setMode, mode } from 'mode-watcher';
	import { neobrutalism, dark } from '@clerk/themes';
</script>

<header
	class="sticky top-0 z-30 flex h-14 items-center gap-4 border-b bg-background px-4 sm:static sm:h-auto sm:border-0 sm:bg-transparent sm:px-6"
>
	<Sheet.Root>
		<Sheet.Trigger asChild let:builder>
			<Button builders={[builder]} size="icon" variant="outline" class="sm:hidden">
				<PanelLeft class="h-5 w-5" />
				<span class="sr-only">Toggle Menu</span>
			</Button>
		</Sheet.Trigger>
		<Sheet.Content side="left" class="sm:max-w-xs">
			<nav class="grid gap-6 text-lg font-medium">
				<a
					href="##"
					class="group flex h-10 w-10 shrink-0 items-center justify-center gap-2 rounded-full bg-primary text-lg font-semibold text-primary-foreground md:text-base"
				>
					<Package2 class="h-5 w-5 transition-all group-hover:scale-110" />
					<span class="sr-only">Epsilon FM</span>
				</a>
				<a
					href="##"
					class="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
				>
					<House class="h-5 w-5" />
					Dashboard
				</a>
				<a href="##" class="flex items-center gap-4 px-2.5 text-foreground">
					<ShoppingCart class="h-5 w-5" />
					Orders
				</a>
				<a
					href="##"
					class="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
				>
					<Package class="h-5 w-5" />
					Products
				</a>
				<a
					href="##"
					class="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
				>
					<UsersRound class="h-5 w-5" />
					Customers
				</a>
				<a
					href="##"
					class="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
				>
					<FileChartLine class="h-5 w-5" />
					Settings
				</a>
			</nav>
		</Sheet.Content>
	</Sheet.Root>
	{#key $mode}
		<div class="pt-2">
			<OrganizationSwitcher
				appearance={{ baseTheme: $mode === 'dark' ? dark : neobrutalism }}
				hidePersonal={true}
				afterCreateOrganizationUrl="/settings"
				afterSelectOrganizationUrl="/settings"
			/>
		</div>
	{/key}
	<Breadcrumbs></Breadcrumbs>
	<div class="relative ml-auto flex-1 md:grow-0">
		<Search class="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
		<Input
			type="search"
			placeholder="Search..."
			class="w-full rounded-lg bg-background pl-8 md:w-[200px] lg:w-[320px]"
		/>
	</div>
	<DropdownMenu.Root>
		<DropdownMenu.Trigger asChild let:builder>
			<Button builders={[builder]} variant="ghost" size="icon">
				<Sun
					class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
				/>
				<Moon
					class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
				/>
				<span class="sr-only">Toggle theme</span>
			</Button>
		</DropdownMenu.Trigger>
		<DropdownMenu.Content align="end">
			<DropdownMenu.Item on:click={() => setMode('light')}>Light</DropdownMenu.Item>
			<DropdownMenu.Item on:click={() => setMode('dark')}>Dark</DropdownMenu.Item>
			<DropdownMenu.Item on:click={() => resetMode()}>System</DropdownMenu.Item>
		</DropdownMenu.Content>
	</DropdownMenu.Root>
	{#key $mode}
		<UserButton appearance={{ baseTheme: $mode === 'dark' ? dark : neobrutalism }} />
	{/key}
</header>
