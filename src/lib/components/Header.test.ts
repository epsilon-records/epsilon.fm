import { describe, it, expect } from 'vitest';
import Header from './Header.svelte';

describe('Header', () => {
	it('should render', () => {
		expect(Header).toBeTruthy();
	});
});
