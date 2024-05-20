describe('task 4: front and e2e spec', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000')
  })

  it('should trigger correct POST request when "Capture" button is clicked', () => {
      cy.intercept('POST', '/capture_image').as('captureImage')
      cy.get('.mb-32 > :nth-child(1)').click()
      cy.wait('@captureImage').its('response.statusCode').should('eq', 200)
  })

  it('should trigger correct POST request when "Shutdown" button is clicked', () => {
      cy.intercept('POST', '/shutdown').as('shutdown')
      cy.get('.mb-32 > :nth-child(3)').click()
      cy.wait('@shutdown').its('response.statusCode').should('eq', 200)
  })
})