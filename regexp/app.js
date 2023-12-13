/**  Prompt from Copilot Chat
write me a javascript function that will check is an email address is a valid format using regexp. Make the regexp a global variable. 
Also include unit tests with both invalid and valid email addresses and proper comments on how to run the unit tests
*/

// Global regular expression for email validation
const EMAIL_REGEX = /\S+@\S+\.\S+/;

// Function that checks if an email address is valid. Returns true if valid, false otherwise.
function isEmail(email) {
    return EMAIL_REGEX.test(email);
}

// Unit tests for isEmail function. 
// To run these tests, you need to have Jest installed. 
// You can run the tests with the command 'npm test' in your terminal.

describe('isEmail', () => {
    test('validates correct email addresses', () => {
        expect(isEmail('foo@bar.com')).toBe(true);
        expect(isEmail('john.doe@example.com')).toBe(true);
    });

    test('invalidates incorrect email addresses', () => {
        expect(isEmail('foo@@bar.com')).toBe(false);
        expect(isEmail('foobar.com')).toBe(false);
        expect(isEmail('@invalid.com')).toBe(false);
        expect(isEmail('foo@invalid')).toBe(false);
    });
});

// regexp to check for valid phone number of format (xxx) xxx-xxxx
const PHONE_REGEX = /\(\d{3}\) \d{3}-\d{4}/;

// Function that checks if a phone number is valid. Returns true if valid, false otherwise.
function isPhone(phone) {
    return PHONE_REGEX.test(phone);
}

// Unit tests for isPhone function.
// To run these tests, you need to have Jest installed.
// You can run the tests with the command 'npm test' in your terminal.

describe('isPhone', () => {
    test('validates correct phone numbers', () => {
        expect(isPhone('(123) 456-7890')).toBe(true);
        expect(isPhone('(555) 555-5555')).toBe(true);
    });

    test('invalidates incorrect phone numbers', () => {
        expect(isPhone('123-456-7890')).toBe(false);
        expect(isPhone('(123)456-7890')).toBe(false);
        expect(isPhone('(123) 456 7890')).toBe(false);
        expect(isPhone('(123) 456-789')).toBe(false);
        expect(isPhone('123 456-7890')).toBe(false);
    });
}

