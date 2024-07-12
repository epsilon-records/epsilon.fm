<script>
	import logo from '$lib/images/logo.png';
	import github from '$lib/images/github.svg';
	import UserButton from 'clerk-sveltekit/client/UserButton.svelte';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import OrganizationSwitcher from 'clerk-sveltekit/client/OrganizationSwitcher.svelte';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
	import Sun from 'lucide-svelte/icons/sun';
	import Moon from 'lucide-svelte/icons/moon';

	import { resetMode, setMode } from 'mode-watcher';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Button } from '$lib/components/ui/button';
</script>

<header>
	<Navbar>
		<div class="corner pt-2">
			<NavBrand href="/">
				<SignedIn>
					<div class="flex items-center">
						<OrganizationSwitcher
							hidePersonal={true}
							afterCreateOrganizationUrl="/profile"
							afterSelectOrganizationUrl="/profile"
						/>
					</div>
				</SignedIn>
				<SignedOut>
					<img src={logo} class="me-3 h-9 sm:h-9" alt="Epsilon Distribution" />
				</SignedOut>
			</NavBrand>
		</div>
		<div class="flex md:order-2">
			<div class="corner pt-1">
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
			</div>
			<div class="corner pt-2">
				<SignedIn>
					<UserButton afterSignOutUrl="/" />
				</SignedIn>
				<SignedOut>
					<a href="https://github.com/natehouk/epsilon.fm">
						<img class="pb-2" src={github} alt="GitHub" />
					</a>
				</SignedOut>
			</div>
			<NavHamburger />
		</div>
		<NavUl class="order-1 m-2">
			<SignedOut
				><NavLi href="/" active={true}>Home</NavLi>
				<NavLi href="/faq">FAQ</NavLi>
				<NavLi href="/artists">Artists</NavLi>
				<NavLi href="/">Pricing</NavLi></SignedOut
			>
			<SignedIn
				><NavLi href="/profile">Profile</NavLi>
				<NavLi href="/">Releases</NavLi>
				<NavLi href="/">Merch</NavLi>
				<NavLi href="/">Website</NavLi>
				<NavLi href="/">Admin</NavLi></SignedIn
			>
		</NavUl>
	</Navbar>
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
		max-width: 64rem;
	}

	.corner {
		width: 3em;
		height: 3em;
	}

	.corner a {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
	}

	.corner img {
		width: 2em;
		height: 2em;
		object-fit: contain;
	}

	nav {
		display: flex;
		justify-content: center;
		--background: rgba(255, 255, 255, 0.7);
	}

	svg {
		width: 2em;
		height: 3em;
		display: block;
	}

	path {
		fill: var(--background);
	}

	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
		background: var(--background);
		background-size: contain;
	}

	li {
		position: relative;
		height: 100%;
	}

	li[aria-current='page']::before {
		--size: 6px;
		content: '';
		width: 0;
		height: 0;
		position: absolute;
		top: 0;
		left: calc(50% - var(--size));
		border: var(--size) solid transparent;
		border-top: var(--size) solid var(--color-theme-1);
	}

	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 0.5rem;
		color: var(--color-text);
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}
</style>
