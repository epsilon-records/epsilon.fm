<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import { clickOutsideAction } from 'svelte-tel-input/utils';
	import { TelInput, isSelected, normalizedCountries } from 'svelte-tel-input';
	import type {
		DetailedValue,
		CountrySelectEvents,
		CountryCode,
		E164Number,
		TelInputOptions,
		Country
	} from 'svelte-tel-input/types';
	import 'svelte-tel-input/styles/flags.css';

	export let clickOutside = true;
	export let closeOnClick = true;
	export let disabled = false;
	export let detailedValue: DetailedValue | null = null;
	export let value: E164Number | null;
	export let searchPlaceholder: string | null = 'Search';
	export let selectedCountry: CountryCode | null;
	export let valid: boolean;
	export let options: TelInputOptions;
	let searchText = '';
	let isOpen = false;

	$: selectedCountryDialCode =
		normalizedCountries.find((el) => el.iso2 === selectedCountry)?.dialCode || null;

	const toggleDropDown = (e?: Event) => {
		e?.preventDefault();
		if (disabled) return;
		isOpen = !isOpen;
	};

	const closeDropdown = (e?: Event) => {
		if (isOpen) {
			e?.preventDefault();
			isOpen = false;
			searchText = '';
		}
	};

	const selectClick = () => {
		if (closeOnClick) closeDropdown();
	};

	const closeOnClickOutside = () => {
		if (clickOutside) {
			closeDropdown();
		}
	};

	const sortCountries = (countries: Country[], text: string) => {
		const normalizedText = text.trim().toLowerCase();
		if (!normalizedText) {
			return countries.sort((a, b) => a.label.localeCompare(b.label));
		}
		return countries.sort((a, b) => {
			const aNameLower = a.name.toLowerCase();
			const bNameLower = b.name.toLowerCase();
			const aStartsWith = aNameLower.startsWith(normalizedText);
			const bStartsWith = bNameLower.startsWith(normalizedText);
			if (aStartsWith && !bStartsWith) return -1;
			if (!aStartsWith && bStartsWith) return 1;
			const aIndex = aNameLower.indexOf(normalizedText);
			const bIndex = bNameLower.indexOf(normalizedText);
			if (aIndex === -1 && bIndex === -1) return a.id.localeCompare(b.id);
			if (aIndex === -1) return 1;
			if (bIndex === -1) return -1;
			const aWeight = aIndex + (aStartsWith ? 0 : 1);
			const bWeight = bIndex + (bStartsWith ? 0 : 1);
			return aWeight - bWeight;
		});
	};

	const handleSelect = (val: CountryCode, e?: Event) => {
		if (disabled) return;
		e?.preventDefault();
		if (
			selectedCountry === undefined ||
			selectedCountry === null ||
			(typeof selectedCountry === typeof val && selectedCountry !== val)
		) {
			selectedCountry = val;
			onChange(val);
			selectClick();
		} else {
			dispatch('same', { option: val });
			selectClick();
		}
	};

	const dispatch = createEventDispatcher<CountrySelectEvents<CountryCode>>();

	const onChange = (selectedCountry: CountryCode) => {
		dispatch('change', { option: selectedCountry });
	};
</script>

<div
	class="relative flex rounded-lg {valid
		? ``
		: ` ring-1 ring-pink-500 focus-within:ring-1 focus-within:ring-offset-1 focus-within:ring-offset-pink-500/50 dark:ring-pink-500`}"
>
	<div class="flex" use:clickOutsideAction={closeOnClickOutside}>
		<button
			id="states-button"
			data-dropdown-toggle="dropdown-states"
			class="relative z-10 inline-flex flex-shrink-0 items-center overflow-hidden whitespace-nowrap rounded-l-lg border border-gray-300 bg-gray-100 px-4 py-2.5 text-center text-sm font-medium text-gray-500 hover:bg-gray-200 focus:outline-none dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600"
			type="button"
			role="combobox"
			aria-controls="dropdown-countries"
			aria-expanded="false"
			aria-haspopup="false"
			on:click={toggleDropDown}
		>
			{#if selectedCountry && selectedCountry !== null}
				<div class="inline-flex items-center text-left">
					<span class="flag flag-{selectedCountry.toLowerCase()} mr-3 flex-shrink-0" />
					{#if options.format === 'national'}
						<span class=" text-gray-600 dark:text-gray-400">+{selectedCountryDialCode}</span>
					{/if}
				</div>
			{:else}
				Please select
			{/if}
			<svg
				aria-hidden="true"
				class="ml-1 h-4 w-4 {isOpen ? 'rotate-180' : ''}"
				fill="currentColor"
				viewBox="0 0 20 20"
				xmlns="http://www.w3.org/2000/svg"
			>
				<path
					fill-rule="evenodd"
					d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
					clip-rule="evenodd"
				/>
			</svg>
		</button>
		{#if isOpen}
			<div
				id="dropdown-countries"
				class="absolute z-10 max-w-fit translate-y-11 divide-y divide-gray-100 overflow-hidden rounded bg-white shadow dark:bg-gray-700"
				data-popper-reference-hidden=""
				data-popper-escaped=""
				data-popper-placement="bottom"
				aria-orientation="vertical"
				aria-labelledby="country-button"
				tabindex="-1"
			>
				<div
					class="max-h-48 overflow-y-auto text-sm text-gray-700 dark:text-gray-200"
					aria-labelledby="countries-button"
					role="listbox"
				>
					<input
						aria-autocomplete="list"
						type="text"
						class="sticky top-0 w-full px-4 py-2 text-gray-900 focus:outline-none"
						bind:value={searchText}
						placeholder={searchPlaceholder}
					/>
					{#each sortCountries(normalizedCountries, searchText) as country (country.id)}
						{@const isActive = isSelected(country.iso2, selectedCountry)}
						<div id="country-{country.iso2}" role="option" aria-selected={isActive}>
							<button
								value={country.iso2}
								type="button"
								class="inline-flex w-full overflow-hidden px-4 py-2 text-sm hover:bg-gray-100
                             active:bg-gray-800 dark:hover:bg-gray-600 dark:active:bg-gray-800
                            {isActive
									? 'bg-gray-600 dark:text-white'
									: 'dark:text-gray-400 dark:hover:text-white'}"
								on:click={(e) => {
									handleSelect(country.iso2, e);
								}}
							>
								<div class="inline-flex items-center text-left">
									<span class="flag flag-{country.iso2.toLowerCase()} mr-3 flex-shrink-0" />
									<span class="mr-2">{country.name}</span>
									<span class="text-gray-500">+{country.dialCode}</span>
								</div>
							</button>
						</div>
					{/each}
				</div>
			</div>
		{/if}
	</div>

	<TelInput
		bind:country={selectedCountry}
		bind:detailedValue
		bind:value
		bind:valid
		{options}
		required
		class="block w-full rounded-r-lg border border-gray-300 border-l-gray-100 bg-gray-50 p-2.5 text-sm text-gray-900 focus:outline-none dark:border-gray-600 dark:border-l-gray-700 
        dark:bg-gray-700 dark:text-white dark:placeholder-gray-400"
	/>
</div>
